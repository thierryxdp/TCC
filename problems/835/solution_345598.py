def melhor_volta(M):
	"""Função em que dada uma Matriz M 6x10 com o tempo em segundos dos corredores em cada volta de uma pista de Kart retorna uma tupla informando de quem foi a melhor voltar, com qual tempo e em qual volta.
	list -> int,int,int"""
	tempos=[]
	m=0
	v=0
	for i in range(len(M)):
		for j in M[i]:
			list.append(tempos,j)
			if m!=min(tempos):
				m=min(tempos)
				if c==i:
					v=0
				v=j+1
				c=i+1
	return (c,m,v)