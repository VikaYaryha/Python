"""Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки. 
Определите, сколько различных слов содержится в этом тексте."""

text = '''She sells sea shells on the sea shore The shells that she sells are
sea shells I'm sure So if she sells sea shells on the sea shore I'm
sure that the shells are sea shore shells'''.lower().split()
result = []
for i in text:
    if i not in result:
        result.append(i)
print(len(result))

# unique_words = set() - множество
# for word in text:
#     unique_words.add(word.lower())
# print(len(unique_words))

# print(len(set(text.lower())))