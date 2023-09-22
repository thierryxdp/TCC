#Start your python function here
def par(num):
    return n % 2 == 0    
def filtra_pares(num):
    pares = ()
    if par(num[0]):
        pares = pares + (num[0],)
    if par(num[1]):
        pares = pares + (num[1],)
    if par(num[2]):
        pares = pares + (num[2],)
    if par(num[3]):
        pares = pares + (num[3],)
    return pares