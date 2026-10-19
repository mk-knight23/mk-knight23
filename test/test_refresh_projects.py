import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('refresh', Path(__file__).resolve().parents[1] / 'scripts/refresh_projects.py')
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.original_root = refresh.ROOT
        self.temp = tempfile.TemporaryDirectory()
        refresh.ROOT = Path(self.temp.name)
        self.readme = refresh.ROOT / 'README.md'
        self.original = 'Keep this intro\n' + refresh.START + '\nold evidence\n' + refresh.END + '\nKeep this footer'
        self.readme.write_text(self.original)
        self.projects = json.loads((self.original_root / 'data/projects.json').read_text())['projects']

    def tearDown(self):
        refresh.ROOT = self.original_root
        self.temp.cleanup()

    def test_only_marked_content_changes(self):
        refresh.render(self.projects, '2026-10-19T12:00:00+00:00')
        text = self.readme.read_text()
        self.assertTrue(text.startswith('Keep this intro\n'))
        self.assertTrue(text.endswith('\nKeep this footer'))
        self.assertIn('MK-QuizFlow', text)
        self.assertTrue((refresh.ROOT / 'data/projects.json').exists())

    def test_incomplete_or_private_metadata_preserves_previous_evidence(self):
        cases = [self.projects[:-1], copy.deepcopy(self.projects)]
        cases[1][0]['private'] = True
        for invalid in cases:
            with self.assertRaises(ValueError):
                refresh.render(invalid, '2026-10-19T12:00:00+00:00')
            self.assertEqual(self.readme.read_text(), self.original)
            self.assertFalse((refresh.ROOT / 'data/projects.json').exists())

    def test_missing_marker_does_not_overwrite_readme(self):
        self.readme.write_text('manual content without markers')
        with self.assertRaises(ValueError):
            refresh.render(self.projects, '2026-10-19T12:00:00+00:00')
        self.assertEqual(self.readme.read_text(), 'manual content without markers')


if __name__ == '__main__':
    unittest.main()
