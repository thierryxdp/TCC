def freq_palavras(frase):
    dic = {}
    frase = frase.split(' ')
    for palavra in frase:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] = dic[palavra] + 1
    return dic