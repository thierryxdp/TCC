def filtraMultiplos(lista,n):
    """ Essa função recebe uma lista e um número n e 
    retorna apenas os múltiplos de n. list,int->list."""
    multiplos = []
    primeiro = lista[0]
    while primeiro%n == 0:
        primeiro = primeiro +1
        multiplos = multiplos + primeiro 
    return multiplos