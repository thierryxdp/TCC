#Start your python function here
def filtra_pares(tupla):
	lista = []
    if tupla[0] % 2 == 0: lista += [tupla[0]]
    if tupla[1] % 2 == 0: lista += [tupla[1]]
    if tupla[2] % 2 == 0: lista += [tupla[2]]
    if tupla[3] % 2 == 0: lista += [tupla[3]]
    return tuple(lista)