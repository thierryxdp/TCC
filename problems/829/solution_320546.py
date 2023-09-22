def soma_h(N):
    '''Função que calcula a soma dos inversos dos números inteiros de 1 até
    N. Entrada: int. Saída: float. '''
    H=0
    for sucessores in range(1,N+1):
        H=H+(1/sucessores)
    return round(H,2)