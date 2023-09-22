#Start your python function here
def filtra_pares(t):
    "Retorna apenas os números pares de uma tupla 't'; tuple -> tuple"
    apenas_pares = tuple(filter(lambda x: x%2 == 0, t))
    return apenas_pares