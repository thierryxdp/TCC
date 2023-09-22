def repetidos (lista):
    rep=[]
    pos=1
    for numero in lista:
        if lista[pos]==lista[(pos-1)]:
            rep=rep+[lista[pos],]
        else:
            rep=rep
        pos=pos+1
    return len(rep)