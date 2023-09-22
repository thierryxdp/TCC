def filtraMultiplos(lista_num, n):
    """função que filtra de uma lista dada como entrada, os multiplos de um número n em uma nova lista; list, int->list"""
    lista_multiplos = []
    indice = 0
    n = int(n)
    while indice < len(lista_num):
        if lista_num[indice]%n == 0:
           lista_multiplos = lista_multiplos + [lista_num[indice],]
        indice = indice + 1
        return lista_multiplos