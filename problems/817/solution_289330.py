def acima_da_media(notas):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da média;
    list, float -> list'''
    if media in notas:
        list.sort(notas)
        i = list.index(notas, media)
        return notas[i+1:]
    elif media not in notas:
        notas = notas + [media]
        list.sort(notas)
        i = list.index(notas, media)
        return notas[i+1:]
    else:
        return []