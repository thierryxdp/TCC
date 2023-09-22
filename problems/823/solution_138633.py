def faltante(lista):
    lista = sorted(lista)
    for n in lista:
        if 1 not in lista:
            return 1
        elif (n + 1) not in lista:
            return n + 1