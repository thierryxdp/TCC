def conta_numero(numero:int,matriz:list)->int:

    """ Função que recebe como entrada um número inteiro e uma matriz e rotarna
        a qantidade de vezes que esse número aparece a matriz.

    """


    nlinhas = len(matriz)
    ncolunas = len(matriz[0])

    qtd = 0

    for i in range(nlinhas):

        for n in range(ncolunas):

            if matriz[i][n] == numero:

                qtd = qtd + 1

    return qtd