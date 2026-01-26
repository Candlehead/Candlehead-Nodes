"""
Aspect Ratio to Resolution Converter Node
Converts aspect ratio text input to fixed resolution values
"""


class AspectToResNode:
    """
    Converts aspect ratio text input to width and height values.
    Supports: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aspect_ratio": ("STRING", {"default": "16:9", "multiline": False}),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "info")
    FUNCTION = "convert_aspect_to_res"
    CATEGORY = "image/resolution"
    
    def convert_aspect_to_res(self, aspect_ratio):
        """Convert aspect ratio text to width and height"""
        
        aspect_map = {
            "1:1": (1328, 1328),
            "16:9": (1664, 928),
            "9:16": (928, 1664),
            "4:3": (1472, 1140),
            "3:4": (1140, 1472),
            "3:2": (1584, 1056),
            "2:3": (1056, 1584),
        }
        
        width, height = aspect_map.get(aspect_ratio.strip(), (1328, 1328))
        info = f"Input: {aspect_ratio.strip()} | Output: {width}×{height}"
        return (width, height, info)
