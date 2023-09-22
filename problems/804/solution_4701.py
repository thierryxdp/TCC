#Start your python function here
def filtra_pares (tupla4):
    """recebe uma tupla com 4 elementos, e retorna uma tupla
    com apenas os valores pares.
    tupla -> tupla"""
    n1 = int(tupla4[0])%2
    n2 = int(tupla4[1])%2
    n3 = int(tupla4[2])%2
    n4 = int(tupla4[3])%2 
    x = ()
    if n1 == 0:
        return x=x+(tupla4[0],)
    if n2 == 0:
        return x=x+(tupla4[1],)
    if n3 == 0:
        return x=x+(tupla4[2],)
    if n4 == 0:
        return x=x+(tupla4[3],)