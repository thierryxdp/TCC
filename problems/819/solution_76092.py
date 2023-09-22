def filtraMultiplos(listaNumeros, num):
    '''Dado uma lista de numeros e um numero, retorna outra lista com os elementos da lista original que sao multiplos do numero.
    list, int -> list'''
    multiplos = []
    i = 0

    while i < len(listaNumeros):
        if (listaNumeros[i] % num) == 0:
            multiplos.append(listaNumeros[i])
        i += 1
    return multiplos