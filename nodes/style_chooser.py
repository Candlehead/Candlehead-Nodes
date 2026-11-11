"""
Style Chooser Node
Selects a style from dropdown and appends custom text input
"""


class StyleChooserNode:
    """
    Combines a dropdown style selection with custom text input.
    The dropdown text is appended with the custom input text.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (
                    [
                        "Modern Comic Book Art",
                        "Anime",
                        "Gil Elvgren",
                        "Boris Vallejo",
                        "Casey Baugh",
                        "Frank Frazetta",
                        "George Hurrell",
                        "Humberto Ramos",
                        "Earle Bergey"
                    ],
                    {"default": "Modern Comic Book Art"}
                ),
                "custom_text": ("STRING", {"default": "", "multiline": True}),
            },
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("style_text", "combined_text")
    FUNCTION = "choose_style"
    CATEGORY = "text/style"
    
    def choose_style(self, style, custom_text):
        """Combine style selection with custom text"""
        
        style_map = {
            "Modern Comic Book Art": "modern comic book art style,",
            "Anime": "anime art style,",
            "Claymation": "claymation art style,",
            "Gil Elvgren": "art style of Gil Elvgren,",
            "Boris Vallejo": "art style of Boris Vallejo,",
            "Casey Baugh": "art style of Casey Baugh,",
            "Frank Frazetta": "art style of Frank Frazetta,",
            "George Hurrell": "art style of George Hurrell,",
            "Humberto Ramos": "art style of Humberto Ramos,",
            "Earle Bergey": "art style of Earle Bergey,",
        }
        
        style_text = style_map.get(style, "modern comic book art style,")
        
        # Append custom text if provided
        if custom_text.strip():
            combined_text = f"{style_text} {custom_text.strip()}"
        else:
            combined_text = style_text.rstrip(",")
        
        return (style_text, combined_text)
