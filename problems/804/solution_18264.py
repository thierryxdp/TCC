#Start your python function here
def filtra_pares(numeros):
    """
    funcao que recebe uma tupla de quatro elementos como 
    parametro, e retorna uma nova tupla contendo apenas os 
    elementos em que se encontravam
    :param numeros: int
    :return: tuple
    """

    numeros = num_1, num_2, num_3, num_4 
    pares = tuple()
    if num_1 % 2 == 0:
        pares += (num1, )
    if num_2 % 2 == 0:
        pares += (num2, )
    if num_3 % 2 == 0:
        pares += (num3, )
    if num_4 % 2 == 0:
        pares += (num4, )
    return pares