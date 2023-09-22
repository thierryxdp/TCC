def primo (n):
    ''' Dado um número inteiro n qualquer
    retorna se este número é primo ou não'''
    for i in range(2,n-1):
        if n % i != 0:
            t = True
        else:
            t = False
    return t