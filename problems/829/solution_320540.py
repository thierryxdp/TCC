def soma_h(N):
    '''Função que calcula H seja H = 1 + 1/2 + 1/3 +..+ 1/N
    int -> float'''
    soma = 0
    for x in range(1/N, 1):
        soma = soma + x
    return x