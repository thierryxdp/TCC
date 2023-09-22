def par(x):
    '''retorna se um número é par ou não'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna o conjunto com
    todos os numeros pares presentes no
    conjunto inicial'''
    Pares=()
    if par(a):
        Pares + (a,)
    elif par(b):
        Pares + (b,)
    elif par(c):
        Pares + (c,)
    elif par(d):
        Pares + (d,)
        return pares