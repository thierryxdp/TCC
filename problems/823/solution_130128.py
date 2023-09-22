def faltante(lista):
    return sum(lista)-sum(list(range(1,lista[-1]+1)))