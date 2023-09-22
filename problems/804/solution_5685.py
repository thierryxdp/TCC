def filtra_pares(tupla):
    lista = []
    for i in range(len(tupla)):
        if tupla[i]%2 == 0:
            lista.append(tupla[i])
    return tuple(lista)