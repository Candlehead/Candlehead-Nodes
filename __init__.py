"""
Candlehead Nodes - ComfyUI Custom Nodes Collection
A suite of utility nodes for image processing, conditioning, and workflow helpers
"""

from .nodes.aspect_converter import AspectToResNode
from .nodes.style_chooser import StyleChooserNode
from .nodes.image_info import ImageInfoNode
from .nodes.text_processor import TextProcessorNode
from .nodes.metadata_parser import MetadataParseFromText
from .nodes.resolution_calculator import ResolutionCalculatorNode
from .nodes.sequential_wildcards import SequentialWildcardsNode
from .nodes.wildcard_prompt import WildcardPromptNode

NODE_CLASS_MAPPINGS = {
    "AspectToRes": AspectToResNode,
    "StyleChooser": StyleChooserNode,
    "ImageInfo": ImageInfoNode,
    "TextProcessor": TextProcessorNode,
    "MetadataParseFromText": MetadataParseFromText,
    "ResolutionCalculator": ResolutionCalculatorNode,
    "SequentialWildcards": SequentialWildcardsNode,
    "WildcardPrompt": WildcardPromptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectToRes": "QWEN Aspect Ratio to Resolution",
    "StyleChooser": "Style Chooser",
    "ImageInfo": "Image Info Extractor",
    "TextProcessor": "Text Processor",
    "MetadataParseFromText": "Metadata Parse from Text",
    "ResolutionCalculator": "Resolution Calculator",
    "SequentialWildcards": "Sequential Wildcards",
    "WildcardPrompt": "Wildcard Prompt",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
