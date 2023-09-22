def faltante(lista) :
    """Dado uma lista com N-1 inteiros numerados de 1 a N,
    determina qual número inteiro desde intervalo está 
    faltando;
    list -> int"""
    list.sort(lista) 
    x = len(lista) - 1
    a = lista[x] 
    L = list(range(1,a+1))
    
    falta = 0
    y = 0 
    
    
    if lista == L:
        return a+1
        
    else :
        while y < len(lista) : 
            if L[y] not in lista :
                falta = L[y]
            y = y + 1
        
        return falta