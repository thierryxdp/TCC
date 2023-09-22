def faltante(lista):
    p = 0
    while lista[p] < len(lista):
        if p+1 == lista[p]:
            p = p + 1
    return p+1