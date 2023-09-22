#Start your python function here
def filtraPares(t):
    """retorna uma tupla com todos os números pares de outra tupla
    tup -> tup"""
    
    pares = ()
    for c in range(len(t)):
        if t[c]%2 == 0:
            pares += (t[c],)
    return pares