def filtraMultiplos(lista,n):
    '''Funçao que dado uma lista retorna outra lista com os multiplos de n 
    list, int -> list'''
    multiplos = []
    indice = 0 
    while indice <len(lista):
        if lista[indice] % n == 0:
            multiplos += (lista[indice],)
        indice = indice + 1
    return multiplos