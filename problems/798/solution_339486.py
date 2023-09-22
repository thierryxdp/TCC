def freq_palavras(string):
    aux1=string.split()
    aux={}
    for x in aux1:
        if x in aux:
            aux[x]+=1
        else:
            aux[x]=1
    return aux