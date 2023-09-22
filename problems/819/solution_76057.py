def filtraMultiplos(lista, n):
    '''Função que recebe uma lista de inteiros e um número n e retorna outra lista com
    os elementos da lista orginal divisiveis por n; list, int -> list'''
    cont = 0
    result = []

    while cont < len(lista):
        if lista[cont]%n == 0:
            result.append(lista[cont])

        cont += 1

    return result