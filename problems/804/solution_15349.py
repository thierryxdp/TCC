#Start your python function here
def filtra_pares(tup):
    """ recebe uma tupla tup com quatro int e retorna uma 
    nova tupla contendo apenas os elementos pares da tupla
    original na mesma ordem em que estavam
    tupla -> tupla"""
    pares = ()
    if tup[0] % 2 == 0:
         pares = pares + (tup[0],)
    if tup[1] % 2 == 0:
         pares = pares + (tup[1],)
    if tup[2] % 2 == 0:
         pares = pares + (tup[2],)
    if tup[3] % 2 == 0:
         pares = pares + (tup[3],)
    return pares