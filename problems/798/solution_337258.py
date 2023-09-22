def freq_palavras(frases):
    letra= ''
    dici= {}
    frases= frases.split(frases.lower())
    for i in frases:
        if i not in dici:
            dici[i] = i.count(letra)
    return dici