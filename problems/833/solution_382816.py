def conta_numero(numero, matriz):
    '''Função na qual dado um número inteiro n e uma matriz retorna
    o número de ocorrência deste número na matriz inserida. int, list
    -> int'''
    soma = 0
    i = 0
    k = 0
    while i <= len(matriz):
        while k <= len(matriz[i]):
            soma = soma + list.count(matriz[i], numero)
            k = k + 1
        i = i + 1
    return soma