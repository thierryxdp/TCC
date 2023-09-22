def faltante(lista):
    k=0
    i=0
    while i<(len(lista)+1):
        k=k+(1+i)
        i=i+1
    return k-sum(lista)