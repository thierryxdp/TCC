def busca(s,M):
	"""Função que recebe uma matriz M contendo os dados de funcionários de uma empresa em formato string em ordem nome, registro, setor e telefone, e faz uma busca pelos funcionários de um setor s e retorna seus dados.
	list -> list"""
	f=[]
	k=-1
	for i in range(len(M)):
		for j in M[i]:
			k=k+1
			if s==j:
				list.append(f,M[i])
				del f[2]
	return f