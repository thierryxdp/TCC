def conta_numero(numero, matriz):
    '''Função na qual dado um número inteiro n e uma matriz retorna
    o número de ocorrência deste número na matriz inserida. int, list
    -> int'''
    soma = 0
    for i in matriz:
        soma += list.count(matriz[i], numero)
    return soma