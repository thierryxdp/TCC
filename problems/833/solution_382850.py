def conta_numero(numero, matriz):
    '''Função na qual dado um número inteiro n e uma matriz retorna
    o número de ocorrência deste número na matriz inserida. int, list
    -> int'''
    soma = 0
    for i in matriz:
        for k in matriz[k]:
            soma = soma + list.count(matriz[k], numero)
    return soma