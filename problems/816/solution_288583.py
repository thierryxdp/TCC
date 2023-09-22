def maiores(lista, n):
    """ Recebe uma lista com números inteiros e um número (n).
    retorna outra lista com todos os numeros da lista orginal maiores que (n).
    list, int --> list """
    listaNova = []
    for elemento in lista :
        if elemento > n:
            list.append(listaNova, elemento)
	list.sort(listaNova)
    return listaNova