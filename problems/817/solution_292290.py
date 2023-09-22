def maiores(lista_inteiros,n):
	"""Função na qual dada uma lista de valores inteiros,
           e um valor inteiro n, retorna uma outra lista com todos os valores
           da lista original maiores que n"""
	colocando = list.append(lista_inteiros,n)
	list.sort(lista_inteiros)
	posicao = list.index(lista_inteiros,n)
	return lista_inteiros[posicao+1:]
def acima_da_media(lista_notas):
	"""Funcao na qual dada uma lista de notas de uma turma,
	   retorn a media da turma e as notas que ficaram acima da media"""
	media = sum(lista_notas)/ len(lista_notas) + 0.1
	lista_maiores_media = maiores(lista_notas,media)
    return lista_maiores_media