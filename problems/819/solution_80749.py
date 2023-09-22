def filtraMultiplos(lista,n):
    """retorna uma lista com todos os elementos da lista original que são multiplos do numero n"""
    """list, int -> lista"""
    i = 0
    multiplos = []
    while (i) < (len(lista)):
        if lista[i] % n == 0:
            multiplos = multiplos + [lista[i],]
        i = i + 1
    return multiplos