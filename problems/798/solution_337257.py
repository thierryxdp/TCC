def freq_palavras(frases):
    letra= ''
    dici= {}
    for i in frases:
        if i not in dici:
            dici[i] = i.count(letra)
    return dici