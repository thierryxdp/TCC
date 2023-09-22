def filtra_pares (t):
    t = (x, y, z, w)
    s = ()
    if x % 2 == 0:
        s = s+(x,)
	if y % 2 == 0:
        s = s+(y,)
	if z % 2 == 0:
        s = s+(z,)
    if w % 2 == 0:
        s = s+(w,)
    return s #Start your python function here