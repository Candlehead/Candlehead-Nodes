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
            "required": {
                "checkpoint_model": (
                    ["Illustrious", "Flux", "Flux 2", "QWEN", "SDXL"],
                    {"default": "Illustrious"},
                ),
            },
            "optional": {
                "aspect_ratio": ("STRING", {"default": "16:9", "multiline": False}),
                "image": ("IMAGE",),
                "width": ("NUMBER",),
                "height": ("NUMBER",),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "Aspect Ratio")
    FUNCTION = "convert_aspect_to_res"
    CATEGORY = "image/resolution"
    
    def convert_aspect_to_res(self, checkpoint_model="Illustrious", aspect_ratio="16:9", image=None, width=None, height=None):
        """Convert aspect ratio text or image to width and height"""
        
        # Preset mappings keyed by checkpoint model
        aspect_maps = {
            "QWEN": {
                "1:1": (1328, 1328),
                "16:9": (1664, 928),
                "9:16": (928, 1664),
                "4:3": (1472, 1140),
                "3:4": (1140, 1472),
                "3:2": (1584, 1056),
                "2:3": (1056, 1584),
            },
            "Flux": {
                "1:1": (1024, 1024),
                "16:9": (1344, 768),
                "9:16": (768, 1344),
                "4:3": (1024, 768),
                "3:4": (768, 1024),
                "3:2": (1216, 832),
                "2:3": (832, 1216),
            },
            "Flux 2": {
                "1:1": (1024, 1024),
                "16:9": (1344, 768),
                "9:16": (768, 1344),
                "4:3": (1024, 768),
                "3:4": (768, 1024),
                "3:2": (1216, 832),
                "2:3": (832, 1216),
            },
            "SDXL": {
                "1:1": (1024, 1024),
                "16:9": (1344, 768),
                "9:16": (768, 1344),
                "4:3": (1182, 886),
                "3:4": (886, 1182),
                "3:2": (1254, 836),
                "2:3": (836, 1254),
            },
            "Illustrious": {
                "1:1": (1024, 1024),
                "16:9": (1344, 768),
                "9:16": (768, 1344),
                "4:3": (1182, 886),
                "3:4": (886, 1182),
                "3:2": (1254, 836),
                "2:3": (836, 1254),
            },
        }
        
        # Select the aspect map for the chosen checkpoint model
        aspect_map = aspect_maps.get(checkpoint_model, aspect_maps["Illustrious"])
        
        # If image is provided, extract dimensions from it
        if image is not None:
            # Image tensor shape is [batch, height, width, channels]
            img_height, img_width = image.shape[1], image.shape[2]
            width = img_width
            height = img_height
            # Display image info
            gcd = math.gcd(int(width), int(height))
            gcd_w = int(width) // gcd
            gcd_h = int(height) // gcd
            aspect_ratio_common = f"{gcd_w}:{gcd_h}"
            image_info = f"Image: {int(width)}×{int(height)} | Aspect: {aspect_ratio_common}"
            print(f"[AspectToRes] {image_info}")
        elif width and height:
            # Use provided width and height
            width = int(width)
            height = int(height)
            gcd = math.gcd(width, height)
            gcd_w = width // gcd
            gcd_h = height // gcd
            aspect_ratio_common = f"{gcd_w}:{gcd_h}"
            image_info = f"Image: {width}×{height} | Aspect: {aspect_ratio_common}"
            print(f"[AspectToRes] {image_info}")
        else:
            # Use text input or default
            output_width, output_height = aspect_map.get(aspect_ratio.strip(), (1328, 1328))
            aspect_ratio_common = aspect_ratio.strip()
            print("[AspectToRes] No image provided - using text input")
            return (output_width, output_height, aspect_ratio_common)
        
        # Calculate aspect ratio from dimensions
        aspect_ratio_calc = width / height
        
        # Calculate simplified ratio
        gcd = math.gcd(int(width), int(height))
        gcd_w = int(width) // gcd
        gcd_h = int(height) // gcd
        aspect_ratio_common = f"{gcd_w}:{gcd_h}"
        
        # Get output resolution from preset or use dimensions
        output_width, output_height = aspect_map.get(aspect_ratio_common.strip(), (1328, 1328))
        
        return (output_width, output_height, aspect_ratio_common)
