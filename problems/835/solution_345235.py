def melhor_volta(m):
	mi = min([j for i in m for j in i])
    return [(m.index(i)+1, mi, i.index(mi)+1) for i in m if mi in i][0]