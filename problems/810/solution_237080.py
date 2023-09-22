def inverte(frase):
    pontuacao = ["!", "?", "...", ".", ",", ":", ";"]
    no_punct = ""
    for char in frase:
       if char not in pontuacao:
           no_punct = no_punct + char
    word_list = no_punct.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    final = str.lower(reversed_sentence)
    final = final.replace('-', ' ')
    return final