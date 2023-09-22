def par(x):
    '''retorna se um número é par ou não'''
    return x%2==0
Pares=()
def filtra_pares(a,b,c,d):
    '''retorna o conjunto com
    todos os numeros pares presentes no
    conjunto inicial'''
    if par(a):
        Pares + (a,)
    elif par(b):
        Pares + (b,)
    elif par(c):
        Pares + (c,)
    elif par(d):
        Pares + (d,)
    else:
        return Pares
    return Pares