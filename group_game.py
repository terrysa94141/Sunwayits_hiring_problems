def find_last_position(number):
    """
    QA部門今天舉辦團康活動,有n個人圍成一圈,順序排號。
    從第一個人開始報數(從1到3報數),凡報到3的人退出圈子。請利用一段程式計算,
    最後留下的那位同事，是所有同事裡面的第幾順位？

    輸入 : n值(0-100)
    輸出 : 第幾順位
    """

    people = list(range(1, number+1))
    # list 中要刪除的 index
    index_to_leave = 0

    while len(people) > 1:
        # 每次跳過2個人，因為是數到3的人出局 所以是 + 3 - 1 = 2
        index_to_leave = (index_to_leave + 2) % len(people)
        people.pop(index_to_leave)

    return people[0]

while True:
    try:
        number = int(input("請輸入人數 (0-100): "))

        if 0 < number <= 100:  # 確保輸入在合理範圍內
            result = find_last_position(number)
            print(f"第{result}順位")
            break

        print("請輸入1到100之間的整數")
    except ValueError:
        print("請輸入有效的整數")
