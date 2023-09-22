def acima_da_media (lista):
    """dada uma lista com a nota dos alunos, diz quais estão acima da média
    list -> list"""
    soma = sum(lista)
    qtd = len(lista)
    media = soma//qtd
    if media in lista:
        list.sort(lista)
        indice = list.index(lista,media)
        lista = lista[indice+1:]
	else:
		list.append (lista,media)
        list.sort(lista)
        indice = list.index(lista,media)
        lista = lista [indice+1:]
	return lista