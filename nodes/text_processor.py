"""
Text Processor Node
Processes and manipulates text strings
"""


class TextProcessorNode:
    """
    Simple text processing node for string manipulation
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "mode": (["uppercase", "lowercase", "capitalize", "reverse"], {"default": "uppercase"}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "process_text"
    CATEGORY = "text"
    
    def process_text(self, text, mode):
        """Process text based on selected mode"""
        
        if mode == "uppercase":
            result = text.upper()
        elif mode == "lowercase":
            result = text.lower()
        elif mode == "capitalize":
            result = text.capitalize()
        elif mode == "reverse":
            result = text[::-1]
        else:
            result = text
        
        return (result,)
