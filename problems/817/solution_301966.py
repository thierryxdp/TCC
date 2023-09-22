def acima_da_media(notas):
    """Função que, dada uma lista com notas de alunos de uma turma, retorne uma lista apenas com as notas que ficaram acima da média;list=>list"""
	media = (sum(notas))/len(notas)
    return sorted(notas,media)