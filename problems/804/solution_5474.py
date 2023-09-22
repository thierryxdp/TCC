#Start your python function here
def filtra_pares(t):
    """Recebe uma tupla com 4 elementos inteiro e 
    retorna outra com somente o elementos pares
    tupla -> tupla"""
    result = ()
    if (t[0]%2) == 0:
        result = result + (t[0],)
    if (t[1]%2) == 0:
        result = result + (t[1],)
    if (t[2]%2) == 0:
        result = result + (t[2],)
    if (t[3]%2) == 0:
        result = result + (t[3],)
    return result