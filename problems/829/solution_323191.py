def soma_h(n):
    '''Dado um número inteiro N, retorna o valor de H com N termos.
    int-->float'''
    H=0
    for termo in range(1,n+1):
        H=H+1/termo
    return round(H,2)