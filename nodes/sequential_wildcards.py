"""
Sequential Wildcards Node
Resolves __wildcard__ tokens from local text files in line order.
"""

import re
from pathlib import Path


WILDCARD_DIRECTORY = Path(r"P:\AI\Wildcards")
WILDCARD_PATTERN = re.compile(r"__(.+?)__")


class SequentialWildcardsNode:
    """Replaces wildcard tokens with successive entries from their files."""

    _cursors = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
            },
            "hidden": {"unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "process_prompt"
    CATEGORY = "text"

    def process_prompt(self, text, unique_id):
        """Resolve each __name__ token using the next name.txt entry."""

        def replace_wildcard(match):
            wildcard_name = match.group(1)
            wildcard_directory = WILDCARD_DIRECTORY.resolve()
            wildcard_file = (wildcard_directory / f"{wildcard_name}.txt").resolve()

            try:
                wildcard_file.relative_to(wildcard_directory)
            except ValueError as error:
                raise ValueError(
                    f"Wildcard path must stay inside {wildcard_directory}: "
                    f"{wildcard_name}"
                ) from error

            if not wildcard_file.is_file():
                raise FileNotFoundError(f"Wildcard file not found: {wildcard_file}")

            choices = [
                line.strip()
                for line in wildcard_file.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            if not choices:
                raise ValueError(f"Wildcard file contains no entries: {wildcard_file}")

            cursor_key = (unique_id, wildcard_file)
            cursor = self._cursors.get(cursor_key, 0)
            self._cursors[cursor_key] = cursor + 1
            return choices[cursor % len(choices)]

        return (WILDCARD_PATTERN.sub(replace_wildcard, text),)
