def melhor_volta(m):
    volta = -1
    minimo = -1
    corredor = -1
    
    for i in m:
        if min(i) < minimo:
            minimo = min(i)
            volta = i.index(minimo)
			corredor = m.index(i)
	return (corredor + 1, minimo, volta + 1)