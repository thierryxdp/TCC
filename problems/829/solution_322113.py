def soma_h(N):
    '''ao receber um número inteiro N, retorna o valor H,
    sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    com somente duas casa decimais
    int -> float'''
    soma = 0
    for i in range(1, N):
        soma = soma + 1/i
    return round(soma, 2)