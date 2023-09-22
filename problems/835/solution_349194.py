def melhor_volta(m):
    """Retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta.
    list -> tuple""""
    v = 1
    p = 1
    t = m[0][0]
	for i in range(len(m)):
        for j in range(len(m[i])):
			if m[i][j] < t:
                t = m[i][j]
                p = i + 1
                v = j + 1
    return (p,t,v)