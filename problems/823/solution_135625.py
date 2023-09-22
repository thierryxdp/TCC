def faltante(L):
    list.append(L,0)
    i=0
    quant=[]
    lista=[]
    while i<(len(L)):
        list.append(quant,i)
        i=i+1
    while not quant[i]==L[i]:
        list.append(lista,i)
        i=i+1
    del lista[1:]
    return int(lista)