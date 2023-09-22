def par(x):
    '''retorna se um número é par ou não'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna o conjunto com
    todos os numeros pares presentes no
    conjunto inicial'''
    pares=(,)
    if par(a):
        pares + (a,)
    elif par(b):
        pares + (b,)
    elif par(c):
        pares + (c,)
    elif par(d):
        pares + (d,)
        return pares