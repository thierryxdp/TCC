def filtra_pares(tup):
    tup = ['a,' 'b,' 'c,' 'd']
    par_a = tup[0]%2==0
    par_b = tup[1]%2==0
    par_c = tup[2]%2==0
    par_d = tup[3]%2==0
    if tup[0] % 2 == 0:
        return tup[0]