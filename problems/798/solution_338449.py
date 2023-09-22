def freq_palavras(frases):
    v={}
    str.split(frases,' ')
    for x in frases:
        v[x]=list.count(frases,x)
    return v