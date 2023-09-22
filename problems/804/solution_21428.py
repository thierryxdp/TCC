def filtra_pares(tupla):
    nova_tup = ()
    i = 0
    while i < len(tupla):
        if tupla[i]%2 == 0:
            nova_tup += tupla[i],
        i += 1
    return nova_tup