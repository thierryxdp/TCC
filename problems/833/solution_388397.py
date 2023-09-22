def conta_numero(numero, matriz):
    """Recebe um número e uma matriz e retorna a quantidade de vezes 
    que esse número aparece na matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[1,1,1], [2,2,2], [3,3,0]]) == 3
    """
    i = 0
    j = 0
    qtde = 0
    for i in range(len(matriz[i])):
        for j in range(len(matriz[i][j]))
        if j == numero:
            i += 1
            qtde += 1
    return qtde