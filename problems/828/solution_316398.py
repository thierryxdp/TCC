def primo (n):
    ''' Dado um número inteiro n, retorna se 
    o mesmo é primo ou não.
    int -> Bool'''
    for i in range(n,n):
        if n%i != 0:
            t = True
        elif n%i == 0:
            t = False
    return t