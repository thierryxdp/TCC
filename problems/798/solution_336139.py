def freq_palavras(frases):
    frase = str.split(frases, ' ')
    di = {}
    for i in frase:
        bo = i in di
        if bo == True:
            di[i] = di[i] + 1
        else:
            di[i] = 1
    return di