def freq_palavras(frases):
    d = dict()
    frases1 = str.split(frases,' ')
    for i in range(len(frases1)):         
        if frases1[i] not in d:
            d[i] = 1
        if frases1[i] in d:
            d[i] += 1
    return d