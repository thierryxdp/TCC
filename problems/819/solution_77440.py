def filtraMultiplos(lista,n):
    """ Essa função recebe uma lista e um número n e 
    retorna apenas os múltiplos de n. list,int->list."""
    multiplos = []
    primeiro = lista[0]
    while primeiro%n == 0:
        multiplos = [multiplos + [lista[0+1],]]
    return multiplos