import unittest
from types import SimpleNamespace

from nodes.resolution_calculator import ResolutionCalculatorNode


class ResolutionCalculatorNodeTests(unittest.TestCase):
    def test_scales_image_dimensions_by_two(self):
        node = ResolutionCalculatorNode()
        image = SimpleNamespace(shape=(1, 800, 600, 4))

        result = node.calculate_resolutions(scale="2x", image=image)

        self.assertEqual(result, (1200, 1600, 1600, 1200))

    def test_scales_image_dimensions_by_four(self):
        node = ResolutionCalculatorNode()
        image = SimpleNamespace(shape=(1, 800, 600, 4))

        result = node.calculate_resolutions(scale="4x", image=image)

        self.assertEqual(result, (2400, 3200, 3200, 2400))

    def test_uses_manual_resolution_when_image_is_missing(self):
        node = ResolutionCalculatorNode()

        result = node.calculate_resolutions(
            scale="2x", width_resolution=640, height_resolution=480
        )

        self.assertEqual(result, (1280, 960, 1280, 960))

    def test_rejects_unsupported_scale(self):
        node = ResolutionCalculatorNode()

        with self.assertRaisesRegex(ValueError, "Unsupported scale"):
            node.calculate_resolutions(scale="3x")


if __name__ == "__main__":
    unittest.main()
