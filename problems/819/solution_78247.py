def filtraMultiplos(numeros, n):
    """Retorna lista contendo todos os elementos da lista original que for divisível pelo número n.
    lista, int --> lista"""
    
    lista_nova = []
    i = 0
    
    while i < len(numeros):
        if numeros[i]%n == 0:
            list.append(lista_nova, numeros[i])
        i = i+1
        
    return lista_nova