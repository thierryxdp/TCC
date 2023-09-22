def soma_h(N):
    '''Calcula e retorna o valor de H = 1 + 1/2 + 1/3 +
    ... + 1/N, com N inteiro e dado como entrada
    int -> float'''
    soma = 0
    for i in range(1, N + 1):
        soma += 1/i
    return soma