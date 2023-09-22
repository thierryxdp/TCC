# Temos uma tupla com 4 elementos inteiros e queremos uma nova tupla com
# apenas seus elementos pares e na mesma ordem em que se encontravam.
# tuple -> tuple

def filtra_pares(tupla):
    '''Dada uma tupla com 4 elementos inteiros, devolve uma nova tupla com
    apenas seus elementos pares e na mesma ordem em que se encontravam;
    tuple -> tuple'''
    if ((tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla
    elif ((tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[: 3]
    elif ((tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[: 2] + tupla[3]
    elif ((tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[0] + tupla[2 :]
    elif ((tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[: 2]
    elif ((tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[0] + tupla[3]
    elif ((tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[0] + tupla[2]
    elif ((tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[0]
    elif (not(tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[1 :]
    elif (not(tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[1] + tupla[3]
    elif (not(tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[1:3]
    elif (not(tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[2:]
    elif (not(tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    (tupla[3] % 2 == 0)):
        return tupla[3]
    elif (not(tupla[0] % 2 == 0) and 
    (tupla[1] % 2 == 0) and 
    not(tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[1]
    elif (not(tupla[0] % 2 == 0) and 
    not(tupla[1] % 2 == 0) and 
    (tupla[2] % 2 == 0) and 
    not(tupla[3] % 2 == 0)):
        return tupla[2]
    else:
        return []