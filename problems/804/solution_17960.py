#Start your python function here
def filtra_pares(num):

    if num[0] % 2 == 0:
       lista = lista + (num[0],)

    if num[1] % 2 == 0:
        lista = lista + (num[1],)

    if num[2] % 2 == 0:
        lista = lista + (num[2],)

    if num[3] % 2 == 0:
        lista = lista + (num[3],)

    return lista