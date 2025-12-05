# ComfyUI Aspect Ratio Switcher Node

A custom node for ComfyUI to switch aspect ratios between landscape and portrait, with official recommended sizes for Qwen Image and WAN2.2 models.

## Core Features

- **Official Recommended Sizes**: Supports Qwen Image and WAN2.2 official recommended resolutions
- **One-click Aspect Ratio Switch**: Easily switch between landscape and portrait modes
- **Conditional Input**: Automatically grays out unavailable input fields based on settings
- **Intuitive UI**: All controls are in Chinese, easy to use
- **Compatible Output**: Directly connect to Latent nodes and other size-dependent nodes

## Supported Preset Sizes

### Qwen Image Official Sizes
- 1:1 - 1328 × 1328
- 16:9 - 1664 × 928  
- 9:16 - 928 × 1664
- 4:3 - 1472 × 1140
- 3:4 - 1140 × 1472

### WAN2.2 Official Sizes
- 1:1 - 1024 × 1024 (default)
- 5:4 - 1152 × 896
- 3:2 - 1216 × 832
- 16:9 - 1344 × 768

## Input Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| Use Default Size | BOOLEAN | True | Switch between preset sizes or custom sizes |
| Default Size | COMBO | qwen 1:1 (1328x1328) | Select from preset sizes |
| Custom Width | INT | 1328 | Custom width input |
| Custom Height | INT | 1328 | Custom height input |
| Using Default Aspect Ratio | BOOLEAN | False | Switch between original and swapped aspect ratio |

## Output Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| width | INT | Output width |
| height | INT | Output height |

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
   ```
   git clone https://github.com/aigirlfriend1118-ui/comfyui-aspect-ratio-switcher.git
   ```

2. Restart ComfyUI

3. Find the node in the "geniusewzq tools" category

## Usage

1. Add the "Aspect Ratio Switcher" node to your workflow
2. Select preset size or input custom dimensions
3. Toggle the aspect ratio switch if needed
4. Connect the output to other nodes requiring size parameters

## Examples

- **Create a 1:1 image for social media**: Select "qwen 1:1 (1328x1328)"
- **Create a portrait video thumbnail**: Select "qwen 9:16 (928x1664)"
- **Create a custom 2000x1500 image**: Disable default size and input custom dimensions
- **Switch orientation**: Toggle the aspect ratio switch to swap width and height

## Compatibility

- Compatible with all ComfyUI versions
- Works with any model that accepts width and height parameters
- Seamless integration with Latent nodes and other size-dependent nodes

## License

MIT License
