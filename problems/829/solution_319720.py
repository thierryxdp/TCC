from math import ceil
def soma_h(N):
    ''' retorna o valor de H com N termos, sendo N o valor de entrada.
    int ->int'''
    h =0
    for i in range(1, N+1):
        h +=(1/i)
    return ceil(h)