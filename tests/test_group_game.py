"""
For group_game.py test
輸入 : n值(0-100)
輸出 : 第幾順位
"""

import pytest
from ..solutions.group_game import find_last_position

def test_find_last_position():
    """
    測試範圍為 1 - 100 ， 100 個都測太多。
    調整為隨機抓幾個，但要包含極端值。
    """
    # 測試案例: 選兩極端值及三個隨機數
    test_cases = [
        {'input': 1, 'expected': 1},
        {'input': 7, 'expected': 4},
        {'input': 10, 'expected': 4},
        {'input': 41, 'expected': 31},
        {'input': 83, 'expected': 40},
        {'input': 100, 'expected': 91}
    ]

    for case in test_cases:
        n = case['input']
        result = find_last_position(n)
        assert (
            result == case['expected']
        ), f"Test failed: input = {n}, expect = {case['expected']}, output = {result}"

    print("test_find_last_position PASS")



def test_find_last_position_invalid_input():
    """測試錯誤輸入的處理"""
    # 非範圍內的整數
    invalid_inputs = [0, -1, -10]
    # 測試非整數型別輸入，但 True/False boolean 值被當整數了
    non_integer_inputs = ["abc", None, [1, 2, 3],True, {"a": 1}]

    # 測試輸入非整數時的情況
    for n in non_integer_inputs:
        with pytest.raises(TypeError, match = "輸入必須是整數"):
            find_last_position(n)

    for n in invalid_inputs:
        with pytest.raises(ValueError, match = "人數必須為 1 到 100 的正整數"):
            find_last_position(n)

    print("test_find_last_position_invalid_input PASS")
