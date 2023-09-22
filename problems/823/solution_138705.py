def faltante(x):
    pecas = 0
    cont = 1

    while cont <= len(x):
        if x[pecas] != cont:
            return cont
            break
        elif cont == len(x):
            return cont + 1
        else:
            pecas += 1
            cont += 1