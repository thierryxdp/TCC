def freq_palavras(frase):
    aux1=string.split()
    aux={}
    for e in aux1:
        if e in aux:
            aux[e]+=1
        else:
            aux[e]=1
    return aux