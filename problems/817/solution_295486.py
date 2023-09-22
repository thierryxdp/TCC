def acima_da_media(lista_alunos):
    '''Dada a lista com as notas dos alunos (lista_alunos), a funcao retorna uma outra lista somente com as notas que ficaram acima da media.
    List -> list.'''
    media = sum(lista_alunos)/len(lista_alunos)
    if media not in lista_alunos:
        list.append(lista_alunos, media)
    list.sort(lista_alunos)
    indice_da_media = list.index(lista_alunos, media)
    return lista_alunos[indice_da_media + 1:]