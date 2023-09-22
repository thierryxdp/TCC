def soma_h(N):
    '''retorna o valor da soma de 1 até 1/N;
int->float'''

    H=0


    for d in range(1,N+1):
        H=H+(1/d)

    return round(H,2)