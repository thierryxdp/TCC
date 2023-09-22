def soma_h(N):
    '''função que retorna o valor da soma com N termos
    int --> float'''
    H = 0
    for i in range(1, N+1):
        H = H + 1/i
    return round(H, 2)