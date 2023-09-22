def acima_da_media (notas: list)->list:
    '''Dada uma lista contendo as notas dos alunos de uma turma, retorna
    uma lista com as que ficaram acima da média'''
    media= sum(notas)/len(notas)
	copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicao= copianotas.index(media)
    maiores= copianotas[posicao + 1:]
    if n in maiores:
        quant= maiores.count(media)
        maiores = maiores[quant:]
    return maiores