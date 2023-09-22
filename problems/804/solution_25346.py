def eh_par(num):
    """retorna True se num for par,false caso contrario int/float ->bool"""
    return num%2==0

def filtra_pares(t):
    """função que recebe uma tupla contendo 4 valores inteiros e devolve uma tupla contendo valores pares da tupla original, na mesma ordem tup->tup"""
    pares=()
    
    if eh_par(t[0]):
        pares = pares +(t[0],)
    if eh_par(t[1]):
        pares = pares +(t[1],)
    if eh_par(t[2]):
        pares = pares +(t[2],)
    if eh_par(t[3]):
        pares = pares +(t[3],)
    return pares