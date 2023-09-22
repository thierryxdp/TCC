def filtra_pares(t):
    t1 = ()
    if t[0] % 2 == 0:
        t1 = t1 + (t[0],)

	if t[1] % 2 == 0:
		t1 = t1 + (t[1],)
	if t[2] % 2 == 0:
        t1 = t1 + (t[2],)
	
	return t1