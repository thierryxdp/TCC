#Start your python function here
def filtra_pares(tupla:tuple)->tuple:
    aux = []
    for k in range(len(tupla)):
        if tupla[k]&1:
            continue
        aux.append(tupla[k])
    return tuple(aux)