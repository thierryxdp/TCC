def faltante(x):
    pecas = 0
    cont = 1

    while cont <= len(x):
        if x[pecas] == cont:
            pecas += 1
            cont += 1
        else:
            return cont