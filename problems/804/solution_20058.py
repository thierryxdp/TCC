def filtra_pares(tupla):
    lista = []
    for elemento in tupla:
        if elemento % 2 == 0:
            lista.append(elemento)
    resultado = tuple(lista)
    return resultado