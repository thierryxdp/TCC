def filtraMultiplos(lista,n):
    """função que retorna uma lista com os multiplos de n
list, int -> list"""
    multiplos = []
    indice = 0
    while indice in lista:
        if indice % n == 0:
            list.append(indice, multiplos )
            indice = indice + 1
    return multiplos