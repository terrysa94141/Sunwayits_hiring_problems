"""
For score reversion test

輸入：[35, 46, 57, 91, 29]
輸出：[53, 64, 75, 19, 92]
"""

from ..solutions.reverse_score import reverse_scores
import pytest

def test_reverse_score():
    """測試是否成功反轉成績"""
    input_scores = [35, 46, 57, 91, 29]
    expected = [53, 64, 75, 19, 92]

    result = reverse_scores(input_scores)

    assert (
        result == expected
        ), f"Test failed: input = {input_scores}, expect = {expected}, result = {result}"

    print("test_reverse_score PASS")
