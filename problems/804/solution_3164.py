def filtra_pares(tupla):
    result = []
    for i in tupla:
        if i%2 == 0:
            result.append(i)
    return tuple(result)