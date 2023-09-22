#Start your python function here
def filtra_pares(tupla):
    """Definição"""
    if tupla[0] % 2 == 0:
        num1 = int(tupla[0])
    if tupla[1] % 2 == 0:
        num2 = int(tupla[1])
    if tupla[2] % 2 == 0:
        num3 = int(tupla[2])
    if tupla[3] % 2 == 0:
        num4 = int(tupla[3])
    return tuple(num1, num2, num3, num4)