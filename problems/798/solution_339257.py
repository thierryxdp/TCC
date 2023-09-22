def freq_palavras(frases):
    """ x """
    dicionario = {}
    lista_palavra = str.split(frases)
    for palavra in lista_palavra:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            dicionario[palavra] = 1
    return dicionario