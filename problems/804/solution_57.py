filtra_pares(tupla):
    tuplafinal = ()
    for i in tupla:
        if i//2 == 0:
            tuplafinal = tuplafinal + (i,)