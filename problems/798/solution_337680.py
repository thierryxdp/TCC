def freq_palavras(frases):
    palavras = frases.split(' ')
    dictResult = {}
    for palavra in palavras:
        if palavra in dictResult:
            dictResult[palavra] += 1
        else:
            dictResult[palavra] = 1
    return dictResult