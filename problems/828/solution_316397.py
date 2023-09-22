def primo (n):
    ''' Dado um número inteiro n, retorna se 
    o mesmo é primo ou não.
    int -> Bool'''
    for i in range(1,n):
        if n%i != 0:
            t = True
        elif n%i == 0:
            t = False
    return t