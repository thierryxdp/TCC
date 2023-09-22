def soma_h(n):
    ''' função que dado um inteiro N, reotrna o somatório da série 1/x, onde
        x começa em 1 e termina em N. int -> float'''
    soma = 0
    for x in range(n + 1):
        termo = 1/x
        if x != 0:
            soma += termo
    return soma