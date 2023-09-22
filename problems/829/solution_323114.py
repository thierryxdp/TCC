def soma_h(N):
    ''' calcula o resultado de uma equação;
    int->float(2 casas decimais)'''
    H=0
    for n in range(1,(N+1)):
        H+=(n)**(-1)
    return round(H,2)