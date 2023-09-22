def filtra_pares(tupla):
    tup_nova = ()
    for num in tupla:
        if num%2 == 0:
            tup_nova += num
    return tup_nova