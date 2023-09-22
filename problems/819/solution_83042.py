def filtraMultiplos(l,n):
    """ Funçao que retorna uma lista  contendo 
    todos os elementos da lista original que foram dividiveis por n"""
    l = []
    multiplos = 0
    list.append(l,n)
    while multiplos < len(l):
        if l[multiplos] % n ==0:
            l = l + (l[multiplos],)
            multiplos = multiplos + 1
            return l