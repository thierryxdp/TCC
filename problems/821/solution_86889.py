def fatorial(n):
    lista=list(range(n+1))
    del lista[0]
    pares=[]
    indice=0
    while indice < len(lista):
        pares=pares*[lista[indice]]
        indice=indice+1        
        return pares