def filtraMultiplos(lista,n):
    """ Funçao que retorna uma lista  contendo todos os elementos da lista original que foram dividiveis por n"""
    n = int
    list2a = []
    multiplos = 0
    while multiplos < len(lista):
        if lista[multiplos] % n == 0:
            lista2 = lista2 + (lista[multiplos],)
            multiplos = multiplos + 1
            return lista2