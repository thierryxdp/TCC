def freq_palavras(frases):
    v={}
    for x in frases:
        v[x]=str.count(frases,x)
    return v