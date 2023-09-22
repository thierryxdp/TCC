def filtra_pares(x):
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    tf = ()
    if a%2 == 0:
        tf = tf + (a,)
    elif b%2 == 0:
        tf = tf + (b,)
    elif c%2 == 0:
        tf= tf + (c,)
    elif d%2 == 0:
        tf= tf + (d,)
        return tf