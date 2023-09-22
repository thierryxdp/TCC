def soma_h(n):
    '''retorna o valor de H com N termos'''
    h = sum( [1/i for i in range(1, n+1) ] )
    return round(h, 2)