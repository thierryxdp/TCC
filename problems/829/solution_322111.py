def soma_h(N):
    '''Função que calcula a soma H = 1 + 1/2 + 1/3 + 1/4 +...+ 1/N, dado o número inteiro N como entrada.
int --> float'''
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
    return round(H,2)