def acima_da_media(lista_notas):
    '''
    função que recebe uma lista com as notas de alunos 
    e retorna a lista ordenada com as notas que ficaram 
    acima da média
    list -> list
    '''
    list.sort(lista_notas)
    media = sum(lista_notas) / len(lista_notas)
	lista_acima_da_media = [lista_notas for lista_notas in lista_notas if lista_notas > media]
    return lista_acima_da_media