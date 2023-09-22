def acima_da_media(lista):
    """função que recebe uma lista com notas dos alunos, e retorna outra lista ordenada com as notas que ficaram
	acima da média
	list -> list"""
    
    media = sum(lista) / len(lista)
    maiores_numeros = list()
    for media in lista:
        if media > len(lista):
            maiores_numeros.append(media)
	list.sort(maiores_numeros)
    
    return maiores_numeros