def inverte(frase):
    word_list = frase.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    print(reversed_sentence