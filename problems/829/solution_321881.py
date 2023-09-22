def soma_h (n):
    '''int-> float'''
    soma=0
    for x in  range(1,n+1):
        soma= soma + x**(-1)
    return round(soma,2)