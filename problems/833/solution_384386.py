def conta_numero(n,m):
    
    r = 0
    for i in range(m):
        for j in range(m[i]):
            if m[i][j] == n:
                r = r + 1
	return r