def freq_palavras(frases):
    """A função retorna quantas vezes uma palavra aparece numa frase;
    str -> dict"""
    i=0
    nls=[]
    nnls=[]
    f=ed5.split(' ')
    f2=ed5.split(' ')
    while i < len(f):
        if f[i] == f2[i]:
            nnls.append(f.count(f[i]))
            nls.append(f2[i])
        i+=1
    return dict(zip(nls,nnls))