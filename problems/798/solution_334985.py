def freq_palavras(frases):
    dicionario = {}
    i = 0
    frase = str.split(frases,)
    while i < len(frase):
        a = list.count(frase, frase[i])
        dicionario[frase[i]] = a
        i = i + 1
    return dicionario