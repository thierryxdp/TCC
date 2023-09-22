def faltante(lista_numeros):
    """
    
    
    
    """
    lista_ideal = list(range(len(lista_numeros)))
    faltante=0
    i=0
    while i<len(lista_numeros):
        if lista_numeros[i]!=lista_ideal[i]:
            faltante=lista_ideal[i]
        i=i+1    
        
    return faltante