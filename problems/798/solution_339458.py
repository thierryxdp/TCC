def freq_palavras(x):
    d={}
    w=x.split()
    for i in w:
        d[i]= dict.get(d,i,0)+1
    return d