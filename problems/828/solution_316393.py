def primo (n):
    ''' Dado um número inteiro n, retorna se 
    o mesmo é primo ou não.
    int -> Bool'''
    for i in range(2,n):
        if n%i != 0:
            t = True
        else:
            t = False
    return t