def faltante(lista) :
    """Dado uma lista com N-1 inteiros numerados de 1 a N,
    determina qual número inteiro desde intervalo está 
    faltanddo;
    list -> int"""
    list.sort(lista) 
    x = len(lista) - 1
    a = lista[x] 
    L = list(range(1,a+1))
    
    falta = 0
    y = 0 
    while y < len(lista) : 
        b = lista[y]
        if b not in L:
            falta = b
        y = y + 1
     
    return falta