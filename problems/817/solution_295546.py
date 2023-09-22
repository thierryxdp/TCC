def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media1 = (sum(notas))//len(notas)
    adicionar = list.append (notas,media)
    um = list.append(notas, media)
    list.sort(notas)
    posicao = list.index(notas, media)
    media2 = notas[posicao+3:]
    media3 = notas[posicao+2:]
    if media1 == 0:
        return []
    else:
        return media