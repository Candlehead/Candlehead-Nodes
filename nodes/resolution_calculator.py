"""
Resolution Calculator Node
Scales image dimensions and reports width, height, long side, and short side.
"""


class ResolutionCalculatorNode:
    """
    Uses image dimensions when available, otherwise falls back to manual values.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scale": (["2x", "4x"],),
            },
            "optional": {
                "image": ("IMAGE",),
                "width_resolution": ("INT", {"default": 1024, "min": 1, "max": 100000}),
                "height_resolution": ("INT", {"default": 1024, "min": 1, "max": 100000}),
            },
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "Long Side", "Short Side")
    FUNCTION = "calculate_resolutions"
    CATEGORY = "image/resolution"

    def calculate_resolutions(
        self, scale, image=None, width_resolution=1024, height_resolution=1024
    ):
        """Return scaled width, height, long side, and short side."""

        if image is not None:
            if hasattr(image, "shape") and len(image.shape) >= 3:
                height = int(image.shape[1])
                width = int(image.shape[2])
            else:
                height = int(width_resolution)
                width = int(height_resolution)
        else:
            height = int(height_resolution)
            width = int(width_resolution)

        multipliers = {"2x": 2, "4x": 4}
        if scale not in multipliers:
            raise ValueError(f"Unsupported scale {scale!r}; choose '2x' or '4x'")

        width *= multipliers[scale]
        height *= multipliers[scale]
        return width, height, max(width, height), min(width, height)
