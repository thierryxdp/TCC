def conta_numero(numero, matriz):
    """Função que retorna quantas vezes um número qualquer escolhido aparece na matriz.

    int, list -> int """

    contador = 0


    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if numero in matriz[i][j]:
                contador = contador + 1


    return contador