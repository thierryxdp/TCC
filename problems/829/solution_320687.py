def soma_h(N):
    '''Funcao que recebe um numero inteiro n, e calcula o valor de H da seguinte equacao:
    H = 1 + 1/2 + 1/3 + ... + 1/N
    int -> float'''
    
    soma = 0

    for i in range(1, N + 1):
        soma += 1 / i
    
    return round(soma, 2)