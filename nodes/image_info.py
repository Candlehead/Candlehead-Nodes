"""
Image Info Extractor Node
Extracts and displays information about images
"""


class ImageInfoNode:
    """
    Analyzes image tensors and outputs dimension and format information
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "channels", "info")
    FUNCTION = "extract_info"
    CATEGORY = "image/info"
    
    def extract_info(self, image):
        """Extract dimensions and channel info from image tensor"""
        
        # Image tensor shape is [batch, height, width, channels]
        batch_size, height, width, channels = image.shape
        
        info_str = f"Batch: {batch_size}, Size: {width}x{height}, Channels: {channels}"
        
        return (width, height, channels, info_str)
