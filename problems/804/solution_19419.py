def filtra_pares(a, b, c, d):
    ''
    t = tuple(a ,b ,c ,d)
    a1 = t[0]%2
    a2 = t[1]%2
    a3 = t[2]%2
    a4 = t[3]%2
    if a1==0 and a2 ==0 and a3==0 and a4==0:
        return (a, b, c, d)