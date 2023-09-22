def filtraMutiplos(lista,numero):
    a=[]
    b=0
    while b<len(lista):
        if lista[b]%numero==0:
            a.append(lista[b])
            b=b+1
    return a