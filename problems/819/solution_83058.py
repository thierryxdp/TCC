def filtraMultiplos(l,n):
    """ Funçao que retorna uma lista  contendo 
    todos os elementos da lista original que foram dividiveis por n"""
    lista= []
    multiplos = 0
    while multiplos < len(l):
        if lista[multiplos] % n:
            lista = list.append(l,n) + (lista[multiplos])
            return lista