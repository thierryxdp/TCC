def conta_numero(numero, matriz):
    """Recebe um número e uma matriz e retorna a quantidade de vezes 
    que esse número aparece na matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[1,1,1], [2,2,2], [3,3,0]]) == 3
    conta_numero(3, [[1,1,1], [2,2,2], [3,3,0]]) == 2
    conta_numero(9, [[9,1], [8,2], [3,3]]) == 1
    """
    qtde = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                qtde += 1
    return qtde