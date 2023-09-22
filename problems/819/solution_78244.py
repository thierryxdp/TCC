def filtraMultiplos(numeros, n):
    """Retorna lista contendo todos os elementos da lista original que for divisível pelo número n.
    lista, int --> lista"""
    
    lista_nova = []
    i = 0
    
    while n > 0:
        if numeros[0]%n == 0:
            list.append(lista_nova, numeros[i])
        i = i+1
        
    return lista_nova