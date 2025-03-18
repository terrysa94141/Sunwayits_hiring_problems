"""
題目 2 - 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間。
文字為"Hello welcome to Cathay 60th year anniversary"。
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數。
"""
def count_appear_time(sentence):
    """將句子轉大寫後分類進字典，最後輸出時再做 sorting"""
    sentence = sentence.upper()
    char_count = {}
    for char in sentence:
        if char.isalnum():  # 檢查是不是數字和字母
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return {k: char_count[k] for k in sorted(char_count.keys())}
