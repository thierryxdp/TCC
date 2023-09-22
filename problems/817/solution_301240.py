def acima_da_media(listanotas):
	'''funcao que dada uma lista com notas dos alunos de uma uma turma,
retorna uma lista com as notas que ficaram acima da média
list,int->list'''
	a=sum(listanotas)
	b= len(listanotas)
	c=a/b
	return maiores(listanotas,c)