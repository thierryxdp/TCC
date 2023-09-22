def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n"""
    
    while i < len(lista):
		mult = list(filter(lambda lista[i]: lista[i] % n == 0, range(lista)))
        
    return mult