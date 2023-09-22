def acima_da_media(lista_alunos):
    lista_alunos_copia = lista_alunos[:]
    '''Dada a lista com as notas dos alunos (lista_alunos), a funcao retorna uma outra lista somente com as notas que ficaram acima da media.
    List -> list.'''
    media = sum(lista_alunos_copia)/len(lista_alunos_copia)
    if media not in lista_alunos_copia:
        list.append(lista_alunos_copia, media)
    list.sort(lista_alunos_copia)
    indice_da_media = list.index(lista_alunos_copia, media)
    return lista_alunos_copia[indice_da_media + 1:]