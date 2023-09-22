def conta_numero(numero, matriz):
    '''Função na qual dado um número inteiro n e uma matriz retorna
    o número de ocorrência deste número na matriz inserida. int, list
    -> int'''
    soma = 0
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            soma = soma + list.count(matriz, numero)
    return soma