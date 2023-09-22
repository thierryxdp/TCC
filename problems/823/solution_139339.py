def faltante(lista):
    """Funçao na qual recebe uma lista com N-1 inteiros em ordem de 1 a N e descobre qual número é faltante
    list -> int"""
    r = 0
    if len(lista) == lista[-1]:
        return lista[-1] + 1
    else:
        while lista[r] == r + 1:
            r = r + 1
        return r + 1