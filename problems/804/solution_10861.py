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
    else:
            conjunto=conjunto
    if par(b):
        conjunto + (b,)
    else:
            conjunto=conjunto
    if par(c):
        conjunto + (c,)
    else:
            conjunto=conjunto
    if par(d):
        conjunto + (d,)
    else:
            conjunto=conjunto
    return conjunto