def acima_da_media(lista):
    """Função em que, dada uma lista com as notas dos alunos de uma turma, retorne uma lista com as notas acima da média;list=>list"""
	media = (sum(lista))/(len(lista))
    return maiores(lista,media)