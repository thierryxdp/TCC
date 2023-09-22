def conta_numero(numero:int,matriz:list)->int:

    """ Função que recebe como entrada um número inteiro e uma matriz e rotarna
        a qantidade de vezes que esse número aparece a matriz.

    """

    qtd = 0

    for j in range(len(matriz)):

        for n in range(len(matriz[0]):

            if matriz[j][n] == numero:

                qtd = qtd + 1

    return qtd