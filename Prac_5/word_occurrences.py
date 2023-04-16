text = input("Text: ")
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_width = max(len(word) for word in word_counts.keys())
for word, count in sorted(word_counts.items()):
    print(f"{word:{max_width}} : {count}")
