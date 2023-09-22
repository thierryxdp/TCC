#Start your python function here
def filtra_pares(tupla:tuple)->tuple:
    aux = []
    for k in range(0, len(tupla), 2):
        aux.append(tupla[k])
    return tuple(aux)