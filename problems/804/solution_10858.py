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
    if par(b):
        conjunto + (b,)
    if par(c):
        conjunto + (c,)
    if par(d):
        conjunto + (d,)
    return conjunto