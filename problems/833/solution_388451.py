def conta_numero(numero,matriz):
    """ função que recebe um número n de uma matriz
    e retorna quantas vezes ele irá aparecer
    nessa matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(0, [[0,10,1], [0,0,1], [0,0,1]]) == 6
    conta_numero(7, [[7,7,2], [7,2,9], [0,0,7]]) == 4
    conta_numero(1, [[1,4,2], [8,7,6], [6,6,1]]) == 2
    """
    contagem = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contagem += 1
    return contagem