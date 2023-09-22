def filtraMultiplos(lista,numero):
    """..."""
    
    num_lista = len(lista)
    indice = 0
    while indice < num_lista:
        if (lista[indice]%numero == 0):
        	indice += 1
    return lista