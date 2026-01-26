"""
Aspect Ratio to Resolution Converter Node
Converts aspect ratio text input or image to fixed resolution values
"""

import math


class AspectToResNode:
    """
    Converts aspect ratio text input or image to width and height values.
    Can accept text input (e.g., "16:9") or an image to analyze.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "aspect_ratio": ("STRING", {"default": "16:9", "multiline": False}),
                "image": ("IMAGE",),
                "width": ("NUMBER",),
                "height": ("NUMBER",),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING", "NUMBER", "FLOAT", "NUMBER", "STRING", "STRING")
    RETURN_NAMES = ("width", "height", "info", "aspect_number", "aspect_float", "is_landscape_bool", "aspect_ratio_common", "aspect_type")
    FUNCTION = "convert_aspect_to_res"
    CATEGORY = "image/resolution"
    
    def convert_aspect_to_res(self, aspect_ratio="16:9", image=None, width=None, height=None):
        """Convert aspect ratio text or image to width and height"""
        
        # Preset mapping for text input
        aspect_map = {
            "1:1": (1328, 1328),
            "16:9": (1664, 928),
            "9:16": (928, 1664),
            "4:3": (1472, 1140),
            "3:4": (1140, 1472),
            "3:2": (1584, 1056),
            "2:3": (1056, 1584),
        }
        
        # If image is provided, extract dimensions from it
        if image is not None:
            # Image tensor shape is [batch, height, width, channels]
            img_height, img_width = image.shape[1], image.shape[2]
            width = img_width
            height = img_height
        elif width and height:
            # Use provided width and height
            width = int(width)
            height = int(height)
        else:
            # Use text input or default
            output_width, output_height = aspect_map.get(aspect_ratio.strip(), (1328, 1328))
            info = f"Input: {aspect_ratio.strip()} | Output: {output_width}×{output_height}"
            # Return defaults for aspect analysis when using text input
            return (
                output_width, 
                output_height, 
                info,
                0,  # aspect_number
                0.0,  # aspect_float
                0,  # is_landscape_bool
                aspect_ratio.strip(),  # aspect_ratio_common
                "unknown"  # aspect_type
            )
        
        # Calculate aspect ratio from dimensions
        aspect_ratio_calc = width / height
        aspect_type = "landscape" if aspect_ratio_calc > 1 else "portrait" if aspect_ratio_calc < 1 else "square"
        
        landscape_bool = 1 if aspect_type == "landscape" else 0
        
        # Calculate simplified ratio
        gcd = math.gcd(width, height)
        gcd_w = width // gcd
        gcd_h = height // gcd
        aspect_ratio_common = f"{gcd_w}:{gcd_h}"
        
        # Get output resolution from preset or use dimensions
        output_width, output_height = aspect_map.get(aspect_ratio_common.strip(), (1328, 1328))
        
        info = f"Input: {aspect_ratio_common} ({aspect_type}) | Output: {output_width}×{output_height}"
        
        return (
            output_width,
            output_height,
            info,
            aspect_ratio_calc,
            aspect_ratio_calc,
            landscape_bool,
            aspect_ratio_common,
            aspect_type
        )
