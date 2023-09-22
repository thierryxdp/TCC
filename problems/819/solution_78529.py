def filtraMultiplos(lista,numero):
    """..."""
    
    num_lista = len(lista)
    indice = 0
    while indice < num_lista:
        if (lista[indice]%numero):
        	indice += 1
    return lista