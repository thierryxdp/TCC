def freq_palavras(f):
    l=str.split(f)
    d={}
    for n in range(len(l)):
        d[l[n]]=str.count(f,l[n])
    return d