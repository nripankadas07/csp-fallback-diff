# csp-fallback-diff

Compare ordered independently enforced policy lists with effective directive fallback origins, first-duplicate handling and added/removed source tokens.

For frontend and platform engineers reviewing csp deployment changes. Changing default-src or child-src affects inherited directives; text diffs can hide which effective lists changed.

## Install and first useful result

Python 3.10+; no runtime dependencies, accounts, API keys or network requests from the tool.
Installation may download setuptools from PyPI. No package has been published to a registry.

```sh
git clone https://github.com/nripankadas07/csp-fallback-diff.git
cd csp-fallback-diff
python -m venv .venv
# POSIX; Windows: .venv\Scripts\activate
. .venv/bin/activate
python -m pip install .
csp-fallback-diff snapshot.json
```

The included fixtures are synthetic. `python demo.py` prints the same real example.
CLI exit codes: 0 = accepted/unchanged, 1 = findings/changed, 2 = invalid input or read failure.
Reports are JSON. Input contracts are explicit; see the included JSON files for their schemas.
Use `--help` for arguments. Paths are local and UTF-8. The tool never writes input/output data.

## Check the implementation

```sh
python verify.py
```

Runs 10 meaningful unit checks, Python compilation, then installs this package into a
new virtual environment and exercises accepted, findings and invalid-input CLI cases outside
the source directory. CI repeats this on Python 3.10, 3.12 and 3.14.

## Limits

Source-list representation comparison only, not a browser, URL matcher or security verdict. No CSP syntax certification, nonce/hash validity, strict-dynamic execution analysis, report-only/meta handling or effective intersection calculation. Policy indexes are paired in supplied order; reordering policies may report changes. Comma-separated policies must first be split into list entries. Hosts and tokens remain case-sensitive; no canonical URL normalization.

See [RESEARCH.md](RESEARCH.md) for the user brief, dated alternatives and tradeoffs;
[VALIDATION.md](VALIDATION.md) for observed check coverage and
[SUPPORT.md](SUPPORT.md) for contribution/security reporting. MIT licensed;
original implementation using the Python standard library, with no competitor code or prose copied.
