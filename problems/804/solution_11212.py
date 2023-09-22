def par(X):
    return x%2==0
def filtra_pares(a,b,c,d):
    conjunto=[]
    if par(a):
        conjunto.append(a)
    else:
        conjunto=conjunto
    if par(b):
        conjunto.append(b)
    else:
        conjunto=conjunto
    if par(c):
        conjunto.append(c)
    else:
        conjunto=conjunto
    if par(d):
        conjunto.append(d)
    else:
        conjunto=conjunto   
    return tuple(conjunto)