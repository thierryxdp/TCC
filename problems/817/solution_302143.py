def acima_da_media(notas_alunos):
    lista_media = list()
    media = sum(notas_alunos)/len(notas_alunos)
    for contador in notas_alunos:
        if contador>media:
            lista_media.append(contador)
    lista_media.sort()
    return lista_media