def soma_h(n):
    ''' função que dado um inteiro N, reotrna o somatório da série 1/x, onde
        x começa em 1 e termina em N. int -> float'''
    soma = 0
    for x in range(n + 1):
        if x != 0:
            termo = 1/x
            soma += termo
    return round(soma,2)