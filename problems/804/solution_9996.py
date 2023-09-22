def filtra_pares(tupla):
    """Recebe uma tupla, com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla
    original, na mesma ordem em que se encontravam;
    tuple -> tuple"""
    a0, a1, a2, a3 = tupla
    if(tupla[0] % 2 != 0):
       a0 = None
    if(tupla[1] % 2 != 0):
       a1 = None
    if(tupla[2] % 2 != 0):
       a2 = None
    if(tupla[3] % 2 != 0):
       a3 = None
    
    return a0, a1, a2, a3