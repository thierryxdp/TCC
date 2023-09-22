#Start your python function here

def filtra_pares(x):
    '''recebe uma tupla de 4 valores e retorna apenas os valores pares'''
    pares = []
    
    if(x[0] % 2 == 0):
        pares.append(x[0])
    if(x[1] % 2 == 0):
        pares.append(x[1])
    if(x[2] % 2 == 0):
        pares.append(x[2])
    if(x[3] % 2 == 0):
        pares.append(x[3])
        
    return tuple(pares)