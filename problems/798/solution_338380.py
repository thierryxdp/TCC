def freq_palavras(frases):
    f = str.split(frases)
    d = {}
    for i in f:
        l=list.count(f,i)
        d[i]=l
    return d