#Start your python function here
def filtra_pares( elementos ):

    lista = []

    for n in elementos:
        if n % 2 == 0:
            lista.append(n)

    return lista