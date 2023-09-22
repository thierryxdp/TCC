def filtraMultiplos(numeros, n):
    """Funcao recebe uma lista com numeros: numeros e um numero qualquer: n
    e retorna uma lista com os numeros da lista original que sao multiplos
    de n """

    lista_multiplos = []

    contador = 0

    while contador < len(numeros):
        if numeros[contador]%n == 0:
            lista_multiplos.append(numeros[contador])
            contador += 1
        else:
            contador += 1

    return lista_multiplos