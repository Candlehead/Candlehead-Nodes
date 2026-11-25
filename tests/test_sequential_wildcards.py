import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nodes.sequential_wildcards import SequentialWildcardsNode


class SequentialWildcardsNodeTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.wildcard_directory = Path(self.temp_directory.name)
        self.directory_patch = patch(
            "nodes.sequential_wildcards.WILDCARD_DIRECTORY",
            self.wildcard_directory,
        )
        self.directory_patch.start()
        self.addCleanup(self.directory_patch.stop)
        self.addCleanup(self.temp_directory.cleanup)
        self.node = SequentialWildcardsNode()

    def test_advances_through_entries_across_executions(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\n\nBob\nCarol\n", encoding="utf-8"
        )

        results = [
            self.node.process_prompt("__people__", unique_id="node-1")[0]
            for _ in range(4)
        ]

        self.assertEqual(results, ["Alice", "Bob", "Carol", "Alice"])

    def test_advances_across_recreated_node_instances(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\nBob\nCarol\n", encoding="utf-8"
        )

        results = [
            SequentialWildcardsNode().process_prompt(
                "__people__", unique_id="node-1"
            )[0]
            for _ in range(3)
        ]

        self.assertEqual(results, ["Alice", "Bob", "Carol"])

    def test_repeated_tokens_consume_successive_entries(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\nBob\nCarol\n", encoding="utf-8"
        )

        result = self.node.process_prompt(
            "__people__ and __people__", unique_id="node-1"
        )

        self.assertEqual(result, ("Alice and Bob",))

    def test_each_wildcard_file_tracks_its_own_position(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\nBob\n", encoding="utf-8"
        )
        (self.wildcard_directory / "places.txt").write_text(
            "Paris\nRome\n", encoding="utf-8"
        )

        first_result = self.node.process_prompt(
            "__people__ in __places__", unique_id="node-1"
        )
        second_result = self.node.process_prompt(
            "__people__ in __places__", unique_id="node-1"
        )

        self.assertEqual(first_result, ("Alice in Paris",))
        self.assertEqual(second_result, ("Bob in Rome",))

    def test_new_node_starts_from_first_entry(self):
        (self.wildcard_directory / "people.txt").write_text(
            "Alice\nBob\n", encoding="utf-8"
        )
        self.node.process_prompt("__people__", unique_id="node-1")

        new_node = SequentialWildcardsNode()

        self.assertEqual(
            new_node.process_prompt("__people__", unique_id="node-2"), ("Alice",)
        )

    def test_raises_for_missing_wildcard_file(self):
        with self.assertRaisesRegex(FileNotFoundError, "Wildcard file not found"):
            self.node.process_prompt("__missing__", unique_id="node-1")

    def test_rejects_paths_outside_wildcard_directory(self):
        with self.assertRaisesRegex(ValueError, "must stay inside"):
            self.node.process_prompt("__..\\outside__", unique_id="node-1")


if __name__ == "__main__":
    unittest.main()
