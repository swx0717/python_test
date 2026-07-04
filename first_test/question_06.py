sentence = input("输入英文句子：")
sentence = sentence.lower()
print(sentence)
sentence = sentence.split()
print(sentence)
counts = []
words = []
for word in sentence:
    if word not in words:
        words.append(word)
        counts.append(1)
    if word in words:
        index = words.index(word)
        counts[index] += 1
counts_words = dict(zip(words, counts))
top_name = max(counts_words, key=counts_words.get)
print(f"{top_name}:{counts_words[top_name]}")
for word, count in counts_words.items():
    if count > 2:
        print(word, count)
