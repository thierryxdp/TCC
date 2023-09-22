def filtraMultiplos(lista,n):
    """ Essa função recebe uma lista e um número n e 
    retorna apenas os múltiplos de n. list,int->list."""
    multiplos = []
    primeiro = [lista[0]]
    while primeiro < len(lista):
        if primeiro%n == 0:
            multiplos = multiplos + primeiro
        primeiro = primeiro +1 
    return multiplos