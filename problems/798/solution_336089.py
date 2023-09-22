def freq_palavras(frases):
    """ """
    frases = " "
    for palavra in range(frases):
        chave = str(palavra)
        valor = list.count(frases, palavra)
        frases = dict(chave, valor)
    return frases