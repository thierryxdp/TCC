def filtra_pares(numeros):
    """
    Função que recebe uma tupla com 4 elementos e vai retornar
    uma nova tupla tendo apenas os pares
    """

    num1, num2, num3, num4 = numeros
    pares = tuple()

    if num1 % 2 == 0:
        pares += (num1, )

    if num2 % 2 == 0:
        pares += (num2, )

    if num3 % 2 == 0:
        pares += (num3, )

    if num4 % 2 == 0:
        pares += (num4, )

    return pares