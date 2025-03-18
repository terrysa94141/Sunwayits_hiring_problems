"""
For count_appear time test
輸入："Hello welcome to Cathay 60th year anniversary"
輸出：{
        '0': 1, '6': 1, 'A': 5, 'C': 2, 'E': 5, 'H': 3, 'I': 1, 'L': 3, 'M': 1, 'N': 2,
        'O': 3, 'R': 3, 'S': 1, 'T': 3, 'V': 1,  'W': 1, 'Y': 3
      }
"""

from ..solutions.count_appear_time import count_appear_time
import pytest

def test_count_appear_time():
    """測試輸出符合預期且字典為 sorted 狀態"""
    message = "Hello welcome to Cathay 60th year anniversary"
    expected = {
        '0': 1, '6': 1, 'A': 5, 'C': 2, 'E': 5, 'H': 3, 'I': 1, 'L': 3, 'M': 1, 'N': 2,
        'O': 3, 'R': 3, 'S': 1, 'T': 3, 'V': 1,  'W': 1, 'Y': 3
    }

    result = count_appear_time(message)

    # 檢查結果與預期的字典內容是否相同
    assert (
        result == expected
    ), f"Test failed: input = {message}, expect = {expected}, output = {result}"

    # 檢查結果的鍵是否已排序
    result_keys = list(result.keys())
    sorted_keys = sorted(result_keys)
    assert (
        result_keys == sorted_keys
    ), f"Test failed: key unsorted, expect = {sorted_keys}, result = {result_keys}"

    print("test_count_appear_time PASS")
