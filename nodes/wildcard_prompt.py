"""
Wildcard Prompt Node
Resolves __wildcard__ tokens from local text files.
"""

import re
import random
from pathlib import Path


WILDCARD_DIRECTORY = Path(r"P:\AI\Wildcards")
WILDCARD_PATTERN = re.compile(r"__(.+?)__")


class WildcardPromptNode:
    """Replaces wildcard tokens with random entries from text files."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xffffffffffffffff,
                        "control_after_generate": True,
                    },
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "process_prompt"
    CATEGORY = "text"

    def process_prompt(self, text, seed=0):
        """Resolve each __name__ token using a corresponding name.txt file."""
        rng = random.Random(seed)

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

            return rng.choice(choices)

        return (WILDCARD_PATTERN.sub(replace_wildcard, text),)
