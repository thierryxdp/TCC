def filtra_pares(t):
	if t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return t
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return t[1:]
    elif t[0]%2!=0 and t[0]%2!=0 and t[2]%2==0 and t[3]%2==0:
		return t[2:]            
    elif t[0]%2!=0 and t[0]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return tuple(t)[3:]