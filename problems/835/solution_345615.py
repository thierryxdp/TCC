def melhor_volta(M):
	"""Função em que dada uma Matriz M 6x10 com o tempo em segundos dos corredores em cada volta de uma pista de Kart retorna uma tupla informando de quem foi a melhor voltar, com qual tempo e em qual volta.
	list -> int,int,int"""
	import copy
	tempos=[]
	m=0
	k=0
	c=1
	for i in range(len(M)):
		for j in M[i]:
			if c==i:
				k=0
			k=k+1
			list.append(tempos,j)
			if m!=min(tempos):
				m=min(tempos)
				v=copy.copy(k)
				c=i+1
	return (c,m,v)