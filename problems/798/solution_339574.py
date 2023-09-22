def freq_palavras(frases):
    s = str.split(frases," ")
    b = {}
    for x in s:
        if x in s:
            b[x] = list.count(s,str(x))
    return b