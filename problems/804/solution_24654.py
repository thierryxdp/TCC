#Start your python function here
def par(x):
    """informa se x é par"""
    return x%2==0

def filtra_pares(t):
    """retorna os valores pares da tupla"""
   
    if par(t[0]):
        tup=tup+(t[0],)
    if par(t[1]):
        tup=tup+(t[1],)
    if par(t[2]):
        tup=tup+(t[2],)
    if par(t[3]):
        tup=tup+(t[3],)
    return tup