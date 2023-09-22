def soma_h(N):
    '''Função que calcula H seja H = 1 + 1/2 + 1/3 +..+ 1/N
    int -> float'''
    soma = 0
    x = 0
    y = 0
    while y >= 1/N or y == 0:
        soma = soma + y
        y = (1 / (x + 1))
        x = x + 1
    return round(soma, 2)