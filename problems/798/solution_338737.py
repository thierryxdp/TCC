def freq_palavras(frases):
    dic = {}
    n = 0
    frases1 = str.split(frases,' ')
    for i in range(len(frases1)):
        if frases1[i] in dic:
            n += 1
        if frases1[i] not in dic:
            dic += {frases1[i]:n,}
    return dic