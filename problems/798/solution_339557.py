def freq_palavras(frases):
    """str -> dict"""
    dicionario = {}
    palavras = frases.split(" ")
    for palavra in palavras:
        if palavra in list(dicionario.keys()):
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario