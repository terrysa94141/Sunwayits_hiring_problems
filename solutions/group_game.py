"""
題目 3 - QA部門今天舉辦團康活動,有n個人圍成一圈,順序排號。
從第一個人開始報數(從1到3報數),凡報到3的人退出圈子。請利用一段程式計算,
最後留下的那位同事，是所有同事裡面的第幾順位？

輸入 : n值(0-100)
輸出 : 第幾順位
"""

def find_last_position(number):
    """
    先檢查輸入，確認為 100 內正整數再往下做。
    圓桌：用 mod 方式
    """
    # 檢查輸入型別，boolean 被當整數來看所以分開檢查
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("輸入必須是整數")

    # 檢查整數是否在範圍內
    if number <= 0 or number > 100:
        raise ValueError("人數必須為 1 到 100 的正整數")

    people = list(range(1, number + 1))
    # list 中要刪除的 index
    index_to_leave = 0

    while len(people) > 1:
        # 每次跳過 2 個人，因為是數到 3 的人出局 所以是 + 3 - 1 = 2
        index_to_leave = (index_to_leave + 2) % len(people)
        people.pop(index_to_leave)

    return people[0]
