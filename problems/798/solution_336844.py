def freq_palavras(frase):
    contagem_palavras = {:}
    for palavra in frase:
        if palavra not in contage_palavras:
            contagem_palavras[palavra] = 1
        else:
            contagem_palavras[palavra] += 1
    return contagem_palavras