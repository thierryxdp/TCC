def soma_h(N):
    '''Função que calcula H seja H = 1 + 1/2 + 1/3 +..+ 1/N
    int -> float'''
    soma = 0
    x = 1
    while x >= 1/N:
        soma = soma + x
        x = 1 / (x + 1)
    return round(soma, 2)