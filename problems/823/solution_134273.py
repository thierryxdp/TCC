def faltante(lista):
    """recebe uma lista pra descobrir a peça faltante
    list->int"""
    i=1
    lista.append(0)
    
    while i<len(lista):
        if i != lista[i-1]:
            return i
        
        i=i+1
    return i