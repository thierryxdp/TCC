#Start your python function heredef filtra_pares(tupla):
def filtra_pares(tupla):
    lista_pares = []
    if tupla[0] % 2 == 0:
        lista_pares.append(tupla[0])
    if tupla[1] % 2 == 0:
        lista_pares.append(tupla[1])
    if tupla[2] % 2 == 0:
        lista_pares.append(tupla[2])
    if tupla[3] % 2 == 0:
        lista_pares.append(tupla[3])
    return tuple(lista_pares)