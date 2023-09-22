def filtraMultiplos(lista_num, n):
    """Recebe uma lista de numeros e um numero n, e retorna uma lista com os\n
    numeros da lista original que são divisíveis por n

    list, int (ou float) -> list"""
    i = 0
    multiplos = []
    while (i < len(lista_num)):
        if (lista_num[i]%n == 0):
            list.append(multiplos, lista_num[i])
        i += 1
    return multiplos