# Candlehead Nodes - ComfyUI Custom Node Collection

A comprehensive suite of utility nodes for ComfyUI image processing workflows.

## Nodes Included

### AspectToRes
Converts aspect ratio text input to fixed width and height values for standard QWEN resolutions.

**Input:** Aspect ratio string (e.g., "16:9", "4:3", "1:1")

**Output:**
- `width` (INT)
- `height` (INT)

**Supported Ratios:**
- 1:1 → 1328×1328
- 16:9 → 1664×928
- 9:16 → 928×1664
- 4:3 → 1472×1140
- 3:4 → 1140×1472
- 3:2 → 1584×1056
- 2:3 → 1056×1584
- Default (unsupported) → 1328×1328

### ImageInfo
Extracts and displays dimension and format information from image tensors.

**Input:** Image tensor

**Output:**
- `width` (INT)
- `height` (INT)
- `channels` (INT)
- `info` (STRING) - Formatted info string

### TextProcessor
Simple text processing node for string manipulation.

**Input:** Text string and processing mode

**Output:** Processed text string

**Modes:**
- uppercase
- lowercase
- capitalize
- reverse

### Wildcard Prompt
Replaces ComfyUI-style `__name__` tokens in manually entered text with a
random non-empty line from `P:\AI\Wildcards\name.txt`. Files in relative
subfolders can be referenced with paths such as `__folder/name__`.

**Input:** Prompt text

**Output:** Text with wildcard entries inserted

The seed input includes ComfyUI's standard **control after generate** options
(randomize, increment, decrement, and fixed), with randomize as the default.

### ResolutionCalculator
Scales both dimensions by the selected multiple and reports the resulting dimensions.

**Input:** Scale (`2x` or `4x`), optional image, Width Resolution, Height Resolution

**Output:**
- `width` (INT)
- `height` (INT)
- `Long Side` (INT) - the larger of the scaled width and height
- `Short Side` (INT) - the smaller of the scaled width and height

## Installation

1. Copy this folder to your ComfyUI `custom_nodes` directory:
   ```bash
   cp -r Candlehead-Nodes /path/to/ComfyUI/custom_nodes/
   ```

2. Restart ComfyUI

## Usage

1. In ComfyUI UI, right-click to open the node menu
2. Search for node name (e.g., "Aspect Ratio to Resolution")
3. Click to add to workflow
4. Connect inputs and outputs as needed

## Project Structure

```
candlehead-nodes/
├── __init__.py           # Main node registration
├── nodes/
│   ├── __init__.py
│   ├── aspect_converter.py
│   ├── image_info.py
│   ├── text_processor.py
│   └── wildcard_prompt.py
└── README.md
```

## License

MIT License
