def filtra_pares(lista):

    lis = []

        if numero % 2 != 0:

            lis.append(numero)

        lis = lis + filtra_pares(lista)

    return lis