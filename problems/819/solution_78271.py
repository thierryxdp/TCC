def filtraMultiplos(lista, n):
    """Recebe como entrada uma lista de números e um número, e retorna outra 
    lista contendo todos os elementos da lista original que forem divisíveis por n"""
    """list, int -> list"""
    multiplos = list()
    i = 0
    
    while (i < len(lista)):
        if lista[i] % n == 0:
            list.append(multiplos,lista[i])
            
        i = i + 1
        
    return multiplos