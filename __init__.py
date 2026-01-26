"""
Candlehead Nodez - ComfyUI Custom Nodes Collection
A suite of utility nodes for image processing, conditioning, and workflow helpers
"""

from .nodes.aspect_converter import AspectToResNode
from .nodes.style_chooser import StyleChooserNode
from .nodes.image_info import ImageInfoNode
from .nodes.text_processor import TextProcessorNode

NODE_CLASS_MAPPINGS = {
    "AspectToRes": AspectToResNode,
    "StyleChooser": StyleChooserNode,
    "ImageInfo": ImageInfoNode,
    "TextProcessor": TextProcessorNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectToRes": "QWEN Aspect Ratio to Resolution",
    "StyleChooser": "Style Chooser",
    "ImageInfo": "Image Info Extractor",
    "TextProcessor": "Text Processor",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
