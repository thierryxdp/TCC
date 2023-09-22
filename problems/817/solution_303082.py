def acima_da_media(notas):
    '''função que recebe lista com notas de alunos, calcula as médias e retorna outra lista com as notas que ficaram acima da média. list -> list'''
    notas_media = []
    media = sum(notas)/len(notas)
    for in range(len(notas)):
        if notas[i] > media:
            notas_media.append(notas[i])
    notas_media.sort()
    return(notas_media)