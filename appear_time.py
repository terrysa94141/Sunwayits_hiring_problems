def count_appear_time(sentence):
    """
    國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間。
    文字為"Hello welcome to Cathay 60th year anniversary"。
    請寫一個程式計算每個字母(大小寫視為同個字母)出現次數。
    """

    sentence = sentence.upper()
    char_count = {}
    for char in sentence:
        if char.isalnum():  # 檢查是不是數字和字母
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for char in sorted(char_count.keys()):
        print(char + ' '+str(char_count[char]))

MESSAGE = "Hello welcome to Cathay 60th year anniversary"
count_appear_time(MESSAGE)
