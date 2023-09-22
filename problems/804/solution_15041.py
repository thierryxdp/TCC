def filtra_pares(x):
    '''Dado uma tupla com 4 elementos, retorna
uma nova que contem apenas os elementos que são pares da original
tuple -> tuple'''
    pares = []
    
    if(x[0] % 2 == 0):
        pares.append(x[0])
    if(x[1] % 2 == 0):
        pares.append(x[1])
    if(x[2] % 2 == 0):
        pares.append(x[2])
    if(x[3] % 2 == 0):
        pares.append(x[3])
        
    return tuple(pares)#Start your python function here