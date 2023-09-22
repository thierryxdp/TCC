def conta_numero(numero, matriz):
    """Recebe um número e uma matriz e retorna a quantidade de vezes 
    que esse número aparece na matriz.
    assinatura: int, list --> int
    testes:
    conta_numero(1, [[1,1,1], [2,2,2], [3,3,0]]) == 3
    """
    i = 0
    for numero in range(len(matriz[i])):
        list.count(matriz[i], numero)
        i = i + 1
    return list.count(matriz[i], numero)