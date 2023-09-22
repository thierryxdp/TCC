#Start your python function here
def filtra_pares(tupla:tuple)->tuple:
    aux = []
    if tupla[0]&1 == 0:
        aux.append(tupla[0])
    elif tupla[1]&1 == 0:
    	aux.append(tupla[1])
    elif tupla[2]&1 == 0:
    	aux.append(tupla[2])
    elif tupla[3]&1 == 0:
    	aux.append(tupla[3])
    return tuple(aux)