def faltante(lista):
    """ """
    """ """
    
    i = 0
    
    while i < len(lista):
        if lista[-len(lista)] == lista[-len(lista)+1]:
            return i
        i = i + 1