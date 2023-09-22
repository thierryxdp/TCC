#Start your python function heredef filtra_pares(x):
    a,b,c,d = x
    tup = ()
    if a%2 == 0:
        tup = tup + (a,)
    if b%2 == 0:
        tup = tup + (b,)
	if c%2 == 0:
        tup = tup + (c,)

    if d%2 == 0:
        tup = tup + (d,)
    return tup