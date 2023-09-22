#Start your python function here
def filtra_pares(tupla0, tupla1, tupla2, tupla3):
    tuplas = (tupla0, tupla1, tupla2, tupla3)
    valores_pares = tuple(filter(lambda x: x%2 == 0, tuplas))
    return (valores_pares)