def filtraMultiplos(l,n):
    """ Funçao que retorna uma lista  contendo 
    todos os elementos da lista original que foram dividiveis por n"""
    lista= []
    multiplos = 0
    while multiplos < len(l):
        if l[multiplos] % n ==0:
            lista = list.append(l,n) + (l[multiplos])
            return lista