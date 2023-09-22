def melhor_volta(m):
    melhor = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < melhor:
                melhor = m[i][j]
                r = (j,melhor,i)
	return r