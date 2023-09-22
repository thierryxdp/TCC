#Start your python function here
def filtra_pares(tupla):
    """Definição"""
    if tupla[0] % 2 == 0:
        return tupla[0]
    if tupla[1] % 2 == 0:
        return tupla[1]
    if tupla[2] % 2 == 0:
        return tupla[2]
    if tupla[3] % 2 == 0:
        return tupla[03]
    return tuple(tupla[0], tupla[1], tupla[2], tupla[3])