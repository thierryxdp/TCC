# Função busca

def busca(setor, matriz):
	'''Dada o setor, retorna as informações que a matriz tem sobre aquele setor.
	str, list(list) -> list(list)'''
	pessoas_do_setor = []
	for i in range(len(matriz)):
		if setor in matriz[i][2]:
			pessoas_do_setor.append(matriz[i][:2] + [matriz[i][3]])
	return pessoas_do_setor