def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n"""
    
	mult = list(filter(lambda x: x % n == 0, range(len(lista))))

    return mult