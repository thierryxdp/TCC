def filtraMultiplos(lista,n):
    """ Funçao que retorna uma lista  contendo todos os elementos da lista original que foram dividiveis por n"""
    n = int
    lista = []
    i = 0
    while i < len(lista):
        if lista  % n ==0:
            lista2=lista
            return