def conta_numero(numero, matriz):
    """Recebe um número e uma matriz e retorna a quantidade de vezes 
    que esse número aparece na matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[1,1,1], [2,2,2], [3,3,0]]) == 3
    """
    i = 0
    qtde = 0
    for i in range(len(matriz[i])):
        if i == numero:
            i += 1
            qtde += 1
    return qtde