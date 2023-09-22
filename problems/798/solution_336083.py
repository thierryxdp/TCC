def freq_palavras(frases):
    """ """
    frase = " "
    for palavra in frases:
        chave = palavra
        valor = list.count(palavra)
        frases = dict(chave, valor)
    return frases