def acima_da_media(lista):
    """ função que recebe uma lista com notas de alunos e retorna
    uma lista ordenada com todas as notas que ficaram acima da media.
    list --> list """
    media = sum(lista)/len(lista)
    maioresNotas = []
    for nota in lista:
        if nota > media:
            list.append(maioresNotas, nota)
	list.sort(maioresNotas)
    return maioresNotas