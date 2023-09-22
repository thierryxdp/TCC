def faltante(lista):
    c=0
    while c<len(lista):
        if lista[c]+1 != lista[c+1] and lista[-1]==lista[c]:
            return lista[c]+1
        else:
            c=c+1