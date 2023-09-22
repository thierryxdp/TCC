def conta_numero(numero, matriz):

    lista = []

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[l][c] == numero:
                lista.append(numero)

    return len(lista)