def faltante(lista):
    i = 0
    ramge = list(range(1,lista[-1]+1))
    while i < len(lista):
        if ramge[i] not in lista:
            return ramge[i]
        i = i + 1
    return len(lista)+1