def faltante(L):
    i=0
    quant=[]
    lista=[]
    while (i-1)<len(L):
        quant=quant+[i]
        i=i+1
    while quant[i]==L[i]:
        lista=lista+[i]
        i=i+1
    del lista[1:]
    return int(lista)