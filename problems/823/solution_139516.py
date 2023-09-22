def faltante(lista):
    c=0
    while c<len(lista):
        if arrum[c]+1 != arrum[c+1]:
            return arrum[c]+1
        else:
            c=c+1