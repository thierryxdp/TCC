def freq_palavras(frases):
    contagem = dict()
    palavras = frases.split()

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return count