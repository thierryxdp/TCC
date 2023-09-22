def filtraMultiplos(lista,numero):
    """..."""
    
    num_lista = len(lista)
    i = 0
    while (i <= num_lista):
        if (lista[i]%numero):
    		i += 1
    		return lista