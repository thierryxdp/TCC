def faltante(lista):
    arrum=list.sort(lista)
    c=0
    while c<len(arrum):
        if arrum[c]+1 =! arrum[c+1]:
            return arrum[c]+1
        else:
            c=c+1