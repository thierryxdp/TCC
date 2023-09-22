def melhor_volta(mat):
	melhor_kart = 0
	melhor_tempo = -1
	melhor_volta = -1
	vs1,vs2,vs3= mat[0],mat[1],mat[2]
	t1=min(mat[0])
	t2 = min(mat[1])
	t3 = min(mat[2])
	melhor_tempo = min(t1,t2,t3)
	if melhor_tempo in vs1:
		melhor_kart = 1
		melhor_volta = list.index(t1,melhor_tempo)+1
	return melhor_kart,melhor_tempo, melhor_volta