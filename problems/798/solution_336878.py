def freq_palavras(f):
    l=str.split(f)
    d={}
    m=0
    for n in range(len(l)):
        d[l[n]]=list.count(l,l[n])
    return d