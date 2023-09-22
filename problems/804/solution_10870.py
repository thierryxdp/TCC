def par(x):
    '''retorna se um número é par ou não'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna o conjunto com
    todos os numeros pares presentes no
    conjunto inicial'''
    conjunto=()
    if par(a):
        return conjunto + (a,) 
    else:
        conjunto=conjunto
    if par(b):
        return conjunto + (b,)
    else:
        return conjunto=conjunto
    if par(c):
        return conjunto + (c,)
    else:
        return conjunto=conjunto
    if par(d):
        return conjunto + (d,)
    else:
        return conjunto=conjunto
    return conjunto