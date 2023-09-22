def posLetra(texto,letra,n):
    i=0
    lista=[]
    while i<len(texto):
        if letra == texto[i]:
            lista=lista+[i,]
        i=i+1
    if n>len(lista):
        return -1
    else:
        return lista[n]