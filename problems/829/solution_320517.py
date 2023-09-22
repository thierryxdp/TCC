def soma_h(n):
    '''Escreva um numero natural. A funcao retorna o valor da equacao da foto.
    int -> float'''
    h=0
    for x in range(1,n+1):
        h=h+(1/x)
    return h