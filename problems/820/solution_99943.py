def posLetra(string,letra,n):
    i=0
    indice=0
    while i<len(string):
        x=str.find(string,letra)
        indice=indice+1
        i=i+1
    return indice