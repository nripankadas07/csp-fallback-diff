import unittest
from csp_fallback_diff import effective, diff

class ContractTests(unittest.TestCase):
    def test_worker_fallback(self):
        r=effective("default-src 'none';script-src 'self';child-src https://workers.example","worker-src")
        self.assertEqual(r["origin"],"child-src")
    def test_no_fallback_ancestors(self):
        self.assertFalse(effective("default-src 'none'","frame-ancestors")["restricted"])
    def test_empty_blocks(self):
        self.assertEqual(effective("script-src;default-src *","script-src-elem")["sources"],[])
    def test_first_duplicate(self):
        r=effective("script-src 'self';script-src *","script-src")
        self.assertEqual(r["sources"],["'self'"]);self.assertEqual(r["duplicates"],["script-src"])
    def test_default_change(self):
        r=diff(["default-src 'self'"],["default-src 'none'"],["img-src"])
        self.assertTrue(r["changed"]);self.assertEqual(r["rows"][0]["removed_tokens"],["'self'"])
    def test_reordering_unchanged(self):
        self.assertFalse(diff(["img-src https://a.example https://b.example"],["img-src https://b.example https://a.example"],["img-src"])["changed"])
    def test_multiple_policies_separate(self):
        r=diff(["img-src *","img-src 'self'"],["img-src *","img-src 'none'"],["img-src"])
        self.assertEqual(len(r["rows"]),2);self.assertFalse(r["rows"][0]["changed"])
    def test_new_policy(self):
        r=diff(["img-src *"],["img-src *","img-src 'none'"],["img-src"])
        self.assertIsNone(r["rows"][1]["before"])
    def test_none_with_tokens(self):
        self.assertEqual(effective("img-src 'none' 'self'","img-src")["sources"],["'self'"])
    def test_refuse_policy_list(self):
        with self.assertRaises(ValueError):effective("img-src *, img-src 'none'","img-src")

if __name__=="__main__":unittest.main()
