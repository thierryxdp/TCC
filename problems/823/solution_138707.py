def faltante(listaNumeros):
    nFaltante = 1

    i = 1
    while i <= len(listaNumeros) + 1:
        if i not in listaNumeros:
            nFaltante = i
            break
        i += 1

    return nFaltante