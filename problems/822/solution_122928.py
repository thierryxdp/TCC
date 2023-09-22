def repetidos (lista):
    rep=[]
    pos=1
    for numero in lista:
        if lista[pos]==lista[pos-1]:
            rep=rep+[lista[pos],]
    return len(rep)