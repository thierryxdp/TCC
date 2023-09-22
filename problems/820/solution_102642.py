def posLetra(string,letra,n):
    contagem=0
    modificada=string
    original=string
    
    if str.count(string,letra)<n:
        return -1
    while contagem<n:
        x=str.index(modificada,letra)
        modificada = modificada[x=1:]
        contagem+=1
    return len(original)-len(modificada)-1