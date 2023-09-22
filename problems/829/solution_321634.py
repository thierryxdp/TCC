def soma_h(n):
    '''  Função que calcula a soma uma serie n termos.
    int->flout'''
    H=0
    for i in list(range(1,n+1)):
        H=H+(1/i)
    return round(H,2)