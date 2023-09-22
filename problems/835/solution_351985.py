def melhor_volta(mat):
	melhor_kart = -1
	melhor_tempo = -1
	melhor_volta = -1
	ts = []
	for vs in mat:
		list.append(ts,min(vs))
	melhor_tempo = min(ts)
	i=0
	for vs in mat:
		i=i+1
		if melhor_tempo in vs:
			melhor_kart =1
			melhor_volta = list.index(vs,melhor_tempo)+1
	return melhor_kart,melhor_tempo,melhor_volta