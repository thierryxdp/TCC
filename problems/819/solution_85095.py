def filtraMultiplos(lista,numero):
    c=0
    L=[]
    while c<len(lista):
        if lista[c]%numero==0:
            L = L + [lista[c]]
        c = c + 1
    return L