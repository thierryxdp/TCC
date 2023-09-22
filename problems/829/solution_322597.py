def soma_h(N):
    '''dado um número inteiro positivo N retorna o
    valor o valor de H com N termos.'''
    H=0
    for termo in range(1,N+1):
        H=H+1/termo
    return round(H,2)