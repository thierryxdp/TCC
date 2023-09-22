def filtra_pares(numeros):
    """
    funcao que recebe uma tupla de quatro elementos como 
    parametro, e retorna uma nova tupla contendo apenas os 
    elementos em que se encontravam
    :param numeros: int
    :return: tuple
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