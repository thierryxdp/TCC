def filtraMultiplos(lista,n):
    """função que retorna uma lista com os multiplos de n
list, int -> list"""
    multiplos = []
    indice = lista[0]
    while indice in lista:
        if indice % n == 0:
            list.append(multiplos,indice)
            indice = indice + lista[1:]
    return multiplos