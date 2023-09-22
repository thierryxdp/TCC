def media_matriz(matriz:list)->float:

    """ Função que recebe uma matriz e retorna a média aritimética de todos
        os números da mariz.

    """

    soma = 0
    numerador = 0

    for i in range(len(matriz)):

        for n in range(len(matriz[0])):

            soma = soma + matriz[i][n]
            numerador = numerador + 1

    media = soma/ numerador
    return round(media,2)