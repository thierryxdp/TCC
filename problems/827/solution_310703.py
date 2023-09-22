def qtd_divisores(x):
    lista = []
    for y in range(1, x + 1):
        if x%y == 0:
            lista.append(y)
    return len(lista)