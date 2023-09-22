def soma_h(n):
    ''' Função que calcula e retorna o valor de h com n termos.
    int-->float'''
    h = 0
    for i in range(0,n):
        h = h + (1/(i+1))
    return round(h,2)