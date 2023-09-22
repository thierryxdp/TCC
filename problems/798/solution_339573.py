def freq_palavras(frases):
    s = str.split(frases," ")
    d = {}
    for x in s:
        if x in s:
            d[x] = list.count(s,str(x))
    return d