def freq_palavras(frase):
    contagem_palavras = {}
    for palavra in frase.split():
        if palavra not in contagem_palavras:
            contagem_palavras[palavra] = 1
        else:
            contagem_palavras[palavra] += 1
    return contagem_palavras