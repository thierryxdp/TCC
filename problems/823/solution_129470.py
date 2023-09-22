def faltante(lista):
    a = 0
    if 1 not in lista:
        return 1
    while True:
        if len(lista) - 1 == a:
            break
        if lista[a] + 1 < lista[a + 1]:
            break
        a += 1
    return lista[a] + 1