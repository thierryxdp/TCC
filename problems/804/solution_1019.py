def filtra_pares (tupla):
    '''Retorna uma tupla contendo somente os elementos pares da tupla inserida "tupla" sem mudar a sua ordem inicial;
    tuple -> tuple'''
    guarda_pares = []
    for i in tupla:
        if i % 2 == 0:
            guarda_pares.append(i)
    return tuple(guarda_pares)