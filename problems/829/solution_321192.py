def soma_h(N):
    '''Função que calcula a soma de H sendo H=1+1/2+1/3+...1/N,
    sendo N dado na entrada da função. int-> float'''
    H = 0
    for x in list(range(1,N+1)):
        if x <= N:
            H = H + 1/x
    return round(H,2)