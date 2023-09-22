def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    for i in palavras:
        dicionario[i] = palavras.count(i)
    return dicionario