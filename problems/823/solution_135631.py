def faltante(L):
    i=0
    quant=[]
    lista=[]
    while i<(len(L)):
        quant=quant+[i]
        i=i+1
    while not quant[i]==L[i]:
        lista=lista+[i]
        i=i+1
    del lista[1:]
    return int(lista)