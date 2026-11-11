import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nodes.wildcard_prompt import WildcardPromptNode


class WildcardPromptNodeTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.wildcard_directory = Path(self.temp_directory.name)
        self.directory_patch = patch(
            "nodes.wildcard_prompt.WILDCARD_DIRECTORY",
            self.wildcard_directory,
        )
        self.directory_patch.start()
        self.addCleanup(self.directory_patch.stop)
        self.addCleanup(self.temp_directory.cleanup)
        self.node = WildcardPromptNode()

    def test_replaces_tokens_from_wildcard_files(self):
        (self.wildcard_directory / "people.txt").write_text(
            " Alice \n\nBob\n", encoding="utf-8"
        )
        result = self.node.process_prompt("Portrait of __people__", seed=0)

        self.assertIn(result[0], ("Portrait of Alice", "Portrait of Bob"))

    def test_seed_makes_wildcard_selection_repeatable(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\nBob\nCarol\n", encoding="utf-8"
        )

        first_result = self.node.process_prompt("__people__", seed=42)
        second_result = self.node.process_prompt("__people__", seed=42)

        self.assertEqual(first_result, second_result)

    def test_seed_uses_comfyui_control_after_generate(self):
        seed_input = WildcardPromptNode.INPUT_TYPES()["required"]["seed"]

        self.assertEqual(seed_input[0], "INT")
        self.assertTrue(seed_input[1]["control_after_generate"])
        self.assertEqual(seed_input[1]["default"], 0)

    def test_replaces_repeated_and_nested_path_tokens(self):
        nested_directory = self.wildcard_directory / "styles"
        nested_directory.mkdir()
        (nested_directory / "hair_color.txt").write_text("silver\n", encoding="utf-8")

        result = self.node.process_prompt(
            "__styles/hair_color__ and __styles/hair_color__", seed=123
        )

        self.assertEqual(result, ("silver and silver",))

    def test_raises_for_missing_wildcard_file(self):
        with self.assertRaisesRegex(FileNotFoundError, "Wildcard file not found"):
            self.node.process_prompt("__missing__", seed=0)

    def test_rejects_paths_outside_wildcard_directory(self):
        with self.assertRaisesRegex(ValueError, "must stay inside"):
            self.node.process_prompt("__..\\outside__", seed=0)


if __name__ == "__main__":
    unittest.main()
