#Start your python function here
def filtra_pares(tup):
    filtrado = []
    for num in tup:
        if num % 2 == 0:
            filtrado.append(num)
            return tuple(filtrado)