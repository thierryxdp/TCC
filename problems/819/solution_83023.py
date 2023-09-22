def filtraMultiplos(lista,n):
    """ Funçao que retorna uma lista  contendo todos os elementos da lista original que foram dividiveis por n"""
    n = int
    lista = []
    multiplos = 0
    while multiplos < len(lista):
        if lista[multiplos] % n == 0:
            multiplos = lista + (lista[multiplos],)
            multiplos = multiplos + 1
            return multiplos