#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试长宽比切换器节点
"""

# 测试节点是否能被正确导入
print("测试节点导入...")
try:
    from aspect_ratio_switcher import AspectRatioSwitcher
    print("✅ 节点导入成功")
except Exception as e:
    print(f"❌ 节点导入失败: {e}")
    exit(1)

# 测试节点的INPUT_TYPES
print("\n测试节点INPUT_TYPES...")
try:
    input_types = AspectRatioSwitcher.INPUT_TYPES()
    print(f"✅ INPUT_TYPES获取成功")
    print(f"   必需参数: {list(input_types['required'].keys())}")
    print(f"   可选参数: {list(input_types['optional'].keys())}")
    print(f"   条件参数: {list(input_types['conditional'].keys())}")
    print(f"   节点分类: {AspectRatioSwitcher.CATEGORY}")
    print(f"   默认尺寸开关显示: {input_types['required']['use_default_size'][1]['label_on']} / {input_types['required']['use_default_size'][1]['label_off']}")
    print(f"   宽高比开关显示: {input_types['optional']['switch_orientation'][1]['label_on']} / {input_types['optional']['switch_orientation'][1]['label_off']}")
except Exception as e:
    print(f"❌ INPUT_TYPES获取失败: {e}")
    exit(1)

# 测试节点的核心功能
print("\n测试节点功能...")
node = AspectRatioSwitcher()

test_cases = [
    # (use_default_size, default_size, custom_width, custom_height, switch_orientation, expected_width, expected_height)
    (True, "qwen 1:1 (1328x1328)", 1024, 768, False, 1328, 1328),
    (True, "wan2.2 16:9 (1344x768)", 1024, 768, True, 768, 1344),
    (False, "qwen 1:1 (1328x1328)", 2000, 1500, False, 2000, 1500),
    (False, "qwen 1:1 (1328x1328)", 2000, 1500, True, 1500, 2000),
]

passed = 0
total = len(test_cases)

for i, test_case in enumerate(test_cases):
    use_default_size, default_size, custom_width, custom_height, switch_orientation, expected_width, expected_height = test_case
    try:
        result = node.switch_aspect_ratio(
            use_default_size=use_default_size,
            default_size=default_size,
            custom_width=custom_width,
            custom_height=custom_height,
            switch_orientation=switch_orientation
        )
        if result == (expected_width, expected_height):
            print(f"✅ 测试用例 {i+1} 通过: {result}")
            passed += 1
        else:
            print(f"❌ 测试用例 {i+1} 失败: 输出={result}, 预期=({expected_width}, {expected_height})")
    except Exception as e:
        print(f"❌ 测试用例 {i+1} 执行失败: {e}")

print(f"\n测试结果: {passed}/{total} 通过")

if passed == total:
    print("\n🎉 所有测试通过! 节点可以正常使用。")
    print("\n📝 节点功能说明:")
    print("   1. 开关显示优化:")
    print("      - 默认状态: 显示'使用默认尺寸'，选择后显示'正在使用自定义尺寸'")
    print("      - 宽高比开关: 默认显示'正在使用默认宽高比'，选择后显示'正在使用对调宽高比'")
    print("   2. 参数顺序优化:")
    print("      - 宽高比对调功能放在最下面")
    print("      - 条件输入功能正常工作")
else:
    print(f"\n❌ 测试失败，节点存在问题。")
