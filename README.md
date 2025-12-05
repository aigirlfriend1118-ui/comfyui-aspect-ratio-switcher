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

---

# ComfyUI 长宽比切换器节点

一个用于 ComfyUI 的自定义节点，用于在横屏和竖屏之间切换长宽比，支持 Qwen Image 和 WAN2.2 模型的官方推荐尺寸。

## 核心功能

- **官方推荐尺寸**: 支持 Qwen Image 和 WAN2.2 官方推荐分辨率
- **一键切换长宽比**: 轻松在横屏和竖屏模式之间切换
- **条件输入**: 根据设置自动灰化不可用的输入字段
- **直观的用户界面**: 所有控件均为中文，易于使用
- **兼容的输出**: 直接连接到 Latent 节点和其他依赖尺寸的节点

## 支持的预设尺寸

### Qwen Image 官方尺寸
- 1:1 - 1328 × 1328
- 16:9 - 1664 × 928  
- 9:16 - 928 × 1664
- 4:3 - 1472 × 1140
- 3:4 - 1140 × 1472

### WAN2.2 官方尺寸
- 1:1 - 1024 × 1024 (默认)
- 5:4 - 1152 × 896
- 3:2 - 1216 × 832
- 16:9 - 1344 × 768

## 输入参数

| 参数名称 | 类型 | 默认值 | 描述 |
|---------|------|--------|------|
| 使用默认尺寸 | BOOLEAN | True | 在预设尺寸和自定义尺寸之间切换 |
| 默认尺寸 | COMBO | qwen 1:1 (1328x1328) | 从预设尺寸中选择 |
| 自定义宽度 | INT | 1328 | 自定义宽度输入 |
| 自定义高度 | INT | 1328 | 自定义高度输入 |
| 正在使用默认宽高比 | BOOLEAN | False | 在原始和交换的宽高比之间切换 |

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|------|------|
| width | INT | 输出宽度 |
| height | INT | 输出高度 |

## 安装方法

1. 将此仓库克隆到您的 ComfyUI `custom_nodes` 目录中：
   ```
   git clone https://github.com/aigirlfriend1118-ui/comfyui-aspect-ratio-switcher.git
   ```

2. 重启 ComfyUI

3. 在 "geniusewzq tools" 分类中找到该节点

## 使用方法

1. 将 "长宽比切换器" 节点添加到您的工作流中
2. 选择预设尺寸或输入自定义尺寸
3. 根据需要切换长宽比开关
4. 将输出连接到其他需要尺寸参数的节点

## 使用示例

- **创建社交媒体用 1:1 图像**: 选择 "qwen 1:1 (1328x1328)"
- **创建竖屏视频缩略图**: 选择 "qwen 9:16 (928x1664)"
- **创建自定义 2000x1500 图像**: 禁用默认尺寸并输入自定义尺寸
- **切换方向**: 切换长宽比开关以交换宽度和高度

## 兼容性

- 兼容所有 ComfyUI 版本
- 与任何接受宽度和高度参数的模型配合使用
- 与 Latent 节点和其他依赖尺寸的节点无缝集成

## 许可证

MIT 许可证

---

# ComfyUI アスペクト比切り替えノード

ComfyUI用のカスタムノードで、ランドスケープとポートレートのアスペクト比を切り替えることができ、Qwen ImageおよびWAN2.2モデルの公式推奨サイズをサポートします。

## コア機能

- **公式推奨サイズ**: Qwen ImageおよびWAN2.2の公式推奨解像度をサポート
- **ワンクリックアスペクト比切り替え**: ランドスケープモードとポートレートモードを簡単に切り替え
- **条件付き入力**: 設定に基づいて使用できない入力フィールドを自動的にグレーアウト
- **直感的なUI**: すべてのコントロールは中国語で、使いやすい
- **互換性のある出力**: Latentノードやその他のサイズ依存ノードに直接接続可能

## サポートされているプリセットサイズ

### Qwen Image 公式サイズ
- 1:1 - 1328 × 1328
- 16:9 - 1664 × 928  
- 9:16 - 928 × 1664
- 4:3 - 1472 × 1140
- 3:4 - 1140 × 1472

### WAN2.2 公式サイズ
- 1:1 - 1024 × 1024 (デフォルト)
- 5:4 - 1152 × 896
- 3:2 - 1216 × 832
- 16:9 - 1344 × 768

## 入力パラメータ

| パラメータ | タイプ | デフォルト | 説明 |
|---------|------|--------|------|
| 使用默认尺寸 | BOOLEAN | True | プリセットサイズとカスタムサイズを切り替える |
| 默认尺寸 | COMBO | qwen 1:1 (1328x1328) | プリセットサイズから選択 |
| 自定义宽度 | INT | 1328 | カスタム幅入力 |
| 自定义高度 | INT | 1328 | カスタム高さ入力 |
| 正在使用默认宽高比 | BOOLEAN | False | 元のアスペクト比と交換されたアスペクト比を切り替える |

## 出力パラメータ

| パラメータ | タイプ | 説明 |
|---------|------|------|
| width | INT | 出力幅 |
| height | INT | 出力高さ |

## インストール方法

1. このリポジトリをComfyUIの`custom_nodes`ディレクトリにクローンします：
   ```
   git clone https://github.com/aigirlfriend1118-ui/comfyui-aspect-ratio-switcher.git
   ```

2. ComfyUIを再起動します

3. "geniusewzq tools"カテゴリでノードを見つけます

## 使用方法

1. ワークフローに「アスペクト比切り替え」ノードを追加します
2. プリセットサイズを選択するか、カスタムサイズを入力します
3. 必要に応じてアスペクト比スイッチを切り替えます
4. 出力を他のサイズパラメータを必要とするノードに接続します

## 使用例

- **ソーシャルメディア用1:1画像を作成**: "qwen 1:1 (1328x1328)"を選択
- **ポートレートビデオサムネイルを作成**: "qwen 9:16 (928x1664)"を選択
- **カスタム2000x1500画像を作成**: デフォルトサイズを無効にしてカスタムサイズを入力
- **向きを切り替え**: アスペクト比スイッチを切り替えて幅と高さを交換

## 互換性

- すべてのComfyUIバージョンと互換性があります
- 幅と高さのパラメータを受け入れる任意のモデルと連携します
- Latentノードやその他のサイズ依存ノードとシームレスに統合されます

## ライセンス

MITライセンス
