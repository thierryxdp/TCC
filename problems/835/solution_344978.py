def melhor_volta(m):
    index = -1
    minimo = 0
    for i in m:
        if min(i) < minimo:
            minimo = min(i)
            volta = i.index(minimo)
			corredor = m.index(i)
	return (corredor + 1, minimo, volta + 1)