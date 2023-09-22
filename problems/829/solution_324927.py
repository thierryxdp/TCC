def soma_h(n):
    '''Dado um número inteiro n, retorna o valor de h com n termos
int-> float'''
    H = 0
    for i in range(1,n+1):
        H+=1/n
    return H