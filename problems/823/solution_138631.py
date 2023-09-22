def faltante(lista):
    lista = sorted(lista)
    for n in lista:
        if 1 not in lista:
            lista.append(1)
            lista = sorted(lista)
            return lista
        elif (n + 1) not in lista:
            return n + 1