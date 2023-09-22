def soma_h(N):
    '''funcao que dado um numero N como entrada
    retorna o valor H com N termos
    int->float'''
    h=0
    for elementos in range(1,N+1):
        h=h+1/elementos
    return round(h,2)