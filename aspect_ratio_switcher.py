class AspectRatioSwitcher:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "use_default_size": ("BOOLEAN", {"default": True, "label_on": "使用默认尺寸", "label_off": "正在使用自定义尺寸"}),
            },
            "optional": {
                "default_size": ([
                                  # Qwen Image 官方推荐尺寸
                                  "qwen 1:1 (1328x1328)", "qwen 16:9 (1664x928)", "qwen 9:16 (928x1664)", "qwen 4:3 (1472x1140)", "qwen 3:4 (1140x1472)",
                                  # WAN2.2 官方推荐尺寸
                                  "wan2.2 1:1 (1024x1024)", "wan2.2 5:4 (1152x896)", "wan2.2 3:2 (1216x832)", "wan2.2 16:9 (1344x768)"], {"default": "qwen 1:1 (1328x1328)", "forceInput": False}),
                "custom_width": ("INT", {"default": 1328, "min": 1, "max": 8192, "step": 1, "forceInput": False}),
                "custom_height": ("INT", {"default": 1328, "min": 1, "max": 8192, "step": 1, "forceInput": False}),
                "switch_orientation": ("BOOLEAN", {"default": False, "label_on": "正在使用默认宽高比", "label_off": "正在使用对调宽高比"}),
            },
            "conditional": {
                "use_default_size": {
                    True: [
                        ["default_size"],
                    ],
                    False: [
                        ["custom_width", "custom_height"],
                    ],
                },
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "switch_aspect_ratio"
    CATEGORY = "geniusewzq tools"

    def switch_aspect_ratio(self, use_default_size, default_size="qwen 1:1 (1328x1328)", custom_width=1328, custom_height=1328, switch_orientation=False):
        # 预设尺寸映射
        preset_sizes = {
            # Qwen Image 官方推荐尺寸
            "qwen 1:1 (1328x1328)": (1328, 1328),
            "qwen 16:9 (1664x928)": (1664, 928),
            "qwen 9:16 (928x1664)": (928, 1664),
            "qwen 4:3 (1472x1140)": (1472, 1140),
            "qwen 3:4 (1140x1472)": (1140, 1472),
            
            # WAN2.2 官方推荐尺寸
            "wan2.2 1:1 (1024x1024)": (1024, 1024),
            "wan2.2 5:4 (1152x896)": (1152, 896),
            "wan2.2 3:2 (1216x832)": (1216, 832),
            "wan2.2 16:9 (1344x768)": (1344, 768),
        }

        # 根据开关选择尺寸来源
        if use_default_size:
            width, height = preset_sizes[default_size]
        else:
            width, height = custom_width, custom_height

        # 处理方向切换
        if switch_orientation:
            final_width, final_height = height, width
        else:
            final_width, final_height = width, height

        return (final_width, final_height)

NODE_CLASS_MAPPINGS = {
    "AspectRatioSwitcher": AspectRatioSwitcher,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioSwitcher": "长宽比切换器",
}
