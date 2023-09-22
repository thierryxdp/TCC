def filtraMultiplos(lista,n):
    """ Essa função recebe uma lista e um número n e 
    retorna apenas os múltiplos de n. list,int->list."""
    multiplos = []
    primeiro = 0
    while primeiro < len(lista):
        if lista[primeiro]%n == 0:
            multiplos = multiplos + [lista[primeiro],]
        primeiro = primeiro +1
    return multiplos