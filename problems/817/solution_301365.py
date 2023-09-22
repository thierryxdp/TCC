def acima_da_media(x):
    'Função que recebe uma lista com as notas dos alunos de uma turma, calcula a média e em seguida define as notas que ficaram acima dela.'
    'list->list'
	if len(x)>1:
		m=sum(x)/len(x)
		list.append(x,m)
		list.sort(x)
		z=len(x)
		y=list.index(x,m)
		return x[y+1:z]
	else:
		return []