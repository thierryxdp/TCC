def faltante(lista):
    lista = sorted(lista)
    for n in lista:
        if (n + 1) not in lista:
            return n + 1