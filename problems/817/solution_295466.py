def acima_da_media(lista_alunos):
    '''Dada a lista com as notas dos alunos (lista_alunos), a funcao retorna uma outra lista somente com as notas que ficaram acima da media.
    List -> list.'''
    media = sum(lista_alunos)/len(lista_alunos)
    list.sort(lista_alunos)
    indice_da_media = list.index(lista_alunos, media)
    return lista_alunos[indice_da_media + 1:]