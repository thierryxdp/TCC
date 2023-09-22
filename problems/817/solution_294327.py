def acima_da_media(lista: list)-> list:
    """Dada uma lista com as notas dos alunos de uma turma, a função
    retorna uma lista ordenada com as notas que ficaram acima da média"""
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    posicao = list.index(lista, media)
    if lista[posicao+1] == lista[posicao]:
    	return lista[posicao+2:]
    else:
        return lista[posicao+1:]