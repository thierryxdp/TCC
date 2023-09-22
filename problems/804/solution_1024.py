#Start your python function here
def filtra_pares(tupla):
    """Definição"""
    if tupla[0] % 2 == 0:
        num1 = tupla[0]
    if tupla[1] % 2 == 0:
         num2 = tupla[1]
    if tupla[2] % 2 == 0:
        num3 = tupla[2]
    if tupla[3] % 2 == 0:
        num4 = tupla[3]
    return tuple(num1, num2, num3, num4)