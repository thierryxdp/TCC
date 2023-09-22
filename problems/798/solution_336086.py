def freq_palavras(frases):
    """ """
    frase = " "
    for palavra in frases:
        chave = str(palavra)
        valor = list.count(frases, palavra)
        frases = dict(str(chave), valor)
    return frases