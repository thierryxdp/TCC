#Start your python function here

def filtra_pares(t):
    """função que recebe uma tupla com quatro elementos e retorna os elementos pares dessa tupla
	tupla -> tupla"""
    
    n = ()
    
    if t[0] % 2 == 0:
        n = n + (t[0],)
    if t[1] % 2 == 0:
        n = n + (t[1],)
    if t[2] % 2 == 0:
        n = n + (t[2],)
    if t[3] % 2 == 0:
        n = n + (t[3],)
    
    return n