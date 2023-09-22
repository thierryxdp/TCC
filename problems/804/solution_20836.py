def filtra_pares(tupla_inteiros):
    lista_pares = []
    if tupla_inteiros[0] % 2 == 0:
        lista_pares.append(tupla_inteiros[0])
    if tupla_inteiros[1] % 2 == 0:
        lista_pares.append(tupla_inteiros[1])
    if tupla_inteiros[2] % 2 == 0:
        lista_pares.append(tupla_inteiros[2])
    if tupla_inteiros[3] % 2 == 0:
        lista_pares.append(tupla_inteiros[3])
    return lista_pares