def filtra_pares(lista):

    lis = []

    if len(lista) > 0:

        numero = lista.pop(0)

        if numero % 2 == 0:

            lis.append(numero)

        lis = lis + filtra_pares(lista)

    return lis.replace("[","(")