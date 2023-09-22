def soma_h(N):
    '''retorna o valor da soma de 1 até 1/N;
int->float'''

    d=1
    H=0


    for valor in range(1,N+1):
        H=H+(1/d)
        d=d+1

    return round(H,2)