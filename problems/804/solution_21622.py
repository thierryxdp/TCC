def filtra_pares(it):
    """a função que filtra os números pares de uma tupla de 
    4 numeros
    tuple(4) --> tuple(...)"""
    ret = []
    if(it[0]%2==0):
        list.append(ret,it[0])
    if(it[1]%2==0):
        list.append(ret,it[1])
    if(it[2]%2==0):
        list.append(ret,it[2])
    if(it[3]%2==0):
        list.append(ret,it[3])
    return tuple(ret)