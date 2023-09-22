def repetidos(lista):
    """..."""
    """..."""
    i = 0
    listaNum = 0
    while i < len(lista)-1:
        if lista[i] == lista[i+1]:
            listaNum = listaNum + 1
        i = i + 1   
    
    return listaNum