#Start your python function here
def filtra_pares(tupla):
    result = ()
    if tupla[0]/2 == 0:
        result.append(tupla[0])
    elif tupla[1]/2 == 0:
        result.append(tupla[1])
    elif tupla[2]/2 == 0:
        result.append(tupla[2])
    else tupla[3]/2 == 0:
        result.append(tupla[3])
    return result