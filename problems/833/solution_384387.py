def conta_numero(n,m):
    
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                r = r + 1
	return r