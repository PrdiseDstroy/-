def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word in i or i in root_word:
            same_words += [i]
    print(same_words)
result_1 = single_root_words('Банан','Банановый','Апельсиновый','Бананы')
result_2 = single_root_words('Апельсиновый', 'Апельсин', 'Гречневый', 'Апель')