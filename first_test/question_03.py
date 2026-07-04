# sentence = input("输入字符串:")
#
# print(sentence[0])
# print(sentence[-1])
# print(sentence[0:3])
# print(sentence[-4:-1])
#
# reversed_sentence = sentence[::-1]
# print(reversed_sentence)

text = input()
letters = sum(1 for ch in text if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'))
digits  = sum(1 for ch in text if '0' <= ch <= '9')
spaces  = sum(1 for ch in text if ch == ' ')      # 只统计空格，不统计其他空白
others  = len(text) - letters - digits - spaces
print(letters, digits, spaces, others)