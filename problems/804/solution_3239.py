def filtra_pares(e1,e2,e3,e4):
    tup = (e1,e2,e3,e4)
    tup2 = (i for i in tup if i%2 == 0)
    return tup2