def faltante(lista):
    a = 0
    while True:
        if len(lista) + 1 == a:
            break
        if lista[a] + 1 < lista[a + 1]:
            break
        a += 1
return lista[a - 1] + 1