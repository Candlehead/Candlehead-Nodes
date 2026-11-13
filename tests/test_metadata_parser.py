import unittest

from nodes.metadata_parser import MetadataParseFromText


class MetadataParseFromTextTests(unittest.TestCase):
    def setUp(self):
        self.node = MetadataParseFromText()

    def test_uses_unet_path_when_checkpoint_is_missing(self):
        result = self.node.parse_metadata(
            r'"unet_name": "MOSS\\mossImage_sft_bf16.safetensors"'
        )

        self.assertEqual(result[2], r"MOSS\\mossImage_sft_bf16.safetensors")

    def test_checkpoint_takes_precedence_over_unet_name(self):
        result = self.node.parse_metadata(
            r'"ckpt_name": "models\checkpoint.safetensors", '
            r'"unet_name": "MOSS\unet.safetensors"'
        )

        self.assertEqual(result[2], r"models\checkpoint.safetensors")

    def test_uses_unet_path_when_checkpoint_value_is_empty(self):
        result = self.node.parse_metadata(
            r'"ckpt_name": "", "unet_name": "MOSS\unet.safetensors"'
        )

        self.assertEqual(result[2], r"MOSS\unet.safetensors")


if __name__ == "__main__":
    unittest.main()
