def freq_palavras(frases):
    letras = []
    for i in range(len(frases)):
        if i not in letras:
            list.append(letras,{i: frases.count(i)})
    return letras