def freq_palavras(frase):
    frequencia = {}
    for palavra in frase:
        if palavra not in frequencia:
            frequencia[palavra] = 1
        if palavra in frequencia:
            frequencia[palavra] = frequencia[palavra]+1
    return frequencia