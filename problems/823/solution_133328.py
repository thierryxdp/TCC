def faltante(lista_numeros):
    """
    
    
    
    """
    lista_ideal = list(range(lista_numeros[-1]))
    faltante=0
    i=0
    while i<len(lista_numeros):
        if lista_numeros[i]!=lista_ideal[i]:
            faltante=lista_ideal[i]
        i=i+1    
        
    return faltante