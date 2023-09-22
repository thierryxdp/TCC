def filtra_pares(tupla):
    """Recebe uma tupla, com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla
    original, na mesma ordem em que se encontravam;
    tuple -> tuple"""
    a0, a1, a2, a3 = tupla
    if(tupla[0] % 2 != 0):
       del a0
    if(tupla[1] % 2 != 0):
       del a1
    if(tupla[2] % 2 != 0):
       del a2
    if(tupla[3] % 2 != 0):
       del a3
    
    return a0, a1, a2, a3