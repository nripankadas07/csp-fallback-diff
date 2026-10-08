"""Explain changes in effective CSP source lists and their fallback origins."""
import argparse
import json
import re
from pathlib import Path

FALLBACKS = {
    "script-src-elem": ["script-src-elem", "script-src", "default-src"],
    "script-src-attr": ["script-src-attr", "script-src", "default-src"],
    "style-src-elem": ["style-src-elem", "style-src", "default-src"],
    "style-src-attr": ["style-src-attr", "style-src", "default-src"],
    "worker-src": ["worker-src", "child-src", "script-src", "default-src"],
    "frame-src": ["frame-src", "child-src", "default-src"],
    "child-src": ["child-src", "default-src"],
    **{x: [x, "default-src"] for x in ("script-src", "style-src", "connect-src", "font-src", "img-src", "manifest-src", "media-src", "object-src")},
    **{x: [x] for x in ("default-src", "base-uri", "form-action", "frame-ancestors")},
}


def parse(policy):
    if not isinstance(policy, str) or "," in policy or any(ord(c) < 32 and c not in "\t\r\n" for c in policy):
        raise ValueError("one serialized policy per list item required; comma-separated policies unsupported")
    result, duplicates = {}, []
    for item in policy.split(";"):
        parts = item.split()
        if not parts:
            continue
        name = parts[0].lower()
        if not re.fullmatch(r"[a-z0-9-]+", name):
            raise ValueError("invalid directive name")
        if name in result:
            duplicates.append(name)
        else:
            result[name] = sorted(set(parts[1:]))
    return result, duplicates


def effective(policy, directive):
    if directive not in FALLBACKS:
        raise ValueError("unsupported directive: " + directive)
    parsed, duplicates = parse(policy)
    for origin in FALLBACKS[directive]:
        if origin in parsed:
            sources = parsed[origin]
            # 'none' is ignored when other source expressions accompany it.
            if "'none'" in sources and len(sources) > 1:
                sources = [x for x in sources if x != "'none'"]
            return {"origin": origin, "sources": sources, "restricted": True, "duplicates": duplicates}
    return {"origin": None, "sources": None, "restricted": False, "duplicates": duplicates}


def diff(before, after, directives):
    for policies in (before, after):
        if not isinstance(policies, list) or not policies or not all(isinstance(x, str) for x in policies):
            raise ValueError("nonempty ordered policy lists required")
    if not isinstance(directives, list) or not directives or any(x not in FALLBACKS for x in directives):
        raise ValueError("supported nonempty directive list required")
    # Keep independently enforced policies separate; do not union their allowlists.
    rows = []
    for i in range(max(len(before), len(after))):
        for d in directives:
            b = effective(before[i], d) if i < len(before) else None
            a = effective(after[i], d) if i < len(after) else None
            changed = b != a
            rows.append({"policy_index": i, "directive": d, "before": b, "after": a, "changed": changed,
                         "added_tokens": sorted(set(a["sources"] or []) - set(b["sources"] or [])) if a and b else [],
                         "removed_tokens": sorted(set(b["sources"] or []) - set(a["sources"] or [])) if a and b else []})
    return {"changed": any(x["changed"] for x in rows), "rows": rows, "semantics": "source-list diff, not a browser execution/security verdict"}


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("snapshot"); a = p.parse_args()
    try:
        data = json.loads(Path(a.snapshot).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or set(data) != {"before", "after", "directives"}:
            raise ValueError("snapshot requires before, after, directives only")
        r = diff(**data); print(json.dumps(r, sort_keys=True)); return 1 if r["changed"] else 0
    except (ValueError, OSError, TypeError) as e:
        print(json.dumps({"error": str(e)})); return 2


if __name__ == "__main__":
    raise SystemExit(main())
