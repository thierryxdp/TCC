def primo (n):
    ''' Dado um número inteiro n qualquer
    retorna se este número é primo ou não'''
    for i in range(3,n):
        if n % 2 != 0:
            i = i + 1
            if n % i != 0:
                t = True
        else:
            t = False
    return t