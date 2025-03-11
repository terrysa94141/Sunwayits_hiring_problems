UNFIXED_SCORES = [35, 46, 57, 91, 29]

def reverse_scores(scores):
    """
    題目1 - 成績修正：
    國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]。
    但是老師在輸入成績的時候有誤，把五位學生的成績改成了[35, 46, 57, 91, 29]。
    請用一個函數來將學生的成績修正。

    輸入：[35, 46, 57, 91, 29]
    輸出：[53, 64, 75, 19, 92]
    """

    return int(str(scores)[::-1]) # 先轉成字串才能reverse

correct_scores = [reverse_scores(score) for score in UNFIXED_SCORES]
print(correct_scores)
