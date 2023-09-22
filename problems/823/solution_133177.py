def faltante(lista):
    """ """
    """ """
    
    i = 0
    lista = list.sort(lista)
    
    while (i < len(lista)):
        if lista[i] == lista[i+1] - 1:
            i = i + 1
            
            
            return i