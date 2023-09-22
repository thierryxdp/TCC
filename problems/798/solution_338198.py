def freq_palavras(frases):
    param = str.split(frases, " ")
    temp = {}
    for x in param:
        temp[x] = dict.get(temp, x, 0) + 1

    return temp