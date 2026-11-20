text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
result_words = []
for word in words:
    if word[-1] in ".,":
        new_word = word[:-1] + "ing" + word[-1]
    else:
        new_word = word + "ing"
    result_words.append(new_word)
result = " ".join(result_words)
print(result)

