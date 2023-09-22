#Start your python function here
def pares( tupla ):

    lista = []

    for n in tupla:
        if n % 2 == 0:
            lista.append(n)

    return lista