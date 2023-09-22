#Start your python function heredef filtra_pares(x):
def filtra_pares(x):
    elementos = filter(lambda valor: valor % 2 == 0, t)
    return tuple (elementos)