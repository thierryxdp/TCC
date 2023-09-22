def acima_da_media(lista)
	'''Dada uma lista com as notas dos alunos de uma turma, retorna
	uma lista ordenada com as notas que ficaram acima da média.'''
    média = sum(lista) / range(lista)
    if media not in lista:
        list.append(lista,media)
        list.sort(lista)
        pos = list.index(lista,media)
        return lista[pos+1:]
    else:
        list.sort(lista)
        pos = list.index(lista,media)
        return lista[pos+1:]