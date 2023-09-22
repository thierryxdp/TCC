def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = (sum(notas))//len(notas)
    um = list.append(lista, media)
    list.sort(notas)
    posicao = list.index(notas, media)
    media = lista [posicao+1:]
    return media