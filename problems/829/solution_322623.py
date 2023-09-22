def soma_h(N):
    '''Retorna o valor da soma H dada
    na questao, ate o numero N
    int --> float'''
    H = 1
    n = 2
    while n <= N:
        H = H + 1/n
        n = n + 1
    return H