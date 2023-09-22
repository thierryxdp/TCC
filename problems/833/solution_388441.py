def conta_numero(numero, matriz):
    """Procedimento que recebe um número inteiro (n) e uma matriz, e retorna a quantidade de vezes 
    que esse número aparece nessa matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[1,1,1], [1,1,1], [1,1,1]]) == 9
    conta_numero(4, [[2,2,2], [4,4,4], [6,6,6]]) == 3
    conta_numero(9, [[0,0,0], [0,0,0], [0,0,0]]) == 0
    """
    contagem = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contagem += 1
    return contagem