def filtraMultiplos(lista, n):
    """ Função que recebe uma lista de números e um número e retorna
        outra lista com todos os elementos da lista original. list, float --> list """
    listaNova = []
    for x in lista:
        if x%n == 0:
            listaNova.append(x)
    return listaNova