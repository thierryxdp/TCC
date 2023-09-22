def faltante(lista):
    i = 0
    intervalo = list(range(1,lista[-1]+2))
    while i < len(lista):
        if intervalo[i] not in lista:
            return intervalo[i]
        i = i + 1