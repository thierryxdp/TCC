def filtra_pares(t):
    a = ()
    flag = 0
    if t[0]%2 == 0:
        a[flag] = t[0]
        flag += 1
	if t[1]%2 == 0:
        a[flag] = t[1]	
        flag += 1
	if t[2]%2 == 0:
        a[flag] = t[2]
        flag += 1
	if t[3]%2 == 0:
        a[flag] = t[3]
        flag += 1