def conta_numero(numero, matriz):
    """Procedimento que recebe um número inteiro e uma matriz, e retorna a quantidade de vezes 
    que esse número aparece nessa matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[2,2,2], [1,2,3], [1,1,1]]) == 4
    conta_numero(3, [[3,3,3], [4,4,4], [5,5,5]]) == 3
    conta_numero(1, [[10,10,10], [0,1,2], [0,0,0]]) == 1
    """
    contagem = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contagem += 1
    return contagem