def par(x):
    '''retorna se um número é par ou não'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna o conjunto com
    todos os numeros pares presentes no
    conjunto inicial'''
    conjunto=()
    if par(a):
        conjunto + (a,) 
    elif par(b):
        conjunto + (b,)
    elif par(c):
        conjunto + (c,)
    elif par(d):
        conjunto + (d,)
    return conjunto