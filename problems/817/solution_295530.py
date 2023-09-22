def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = (sum(notas))//len(notas)
    um = list.append(notas, media)
    list.sort(notas)
    if media>0 and media>1:
        posicao = list.index(notas, media-1)
        media = notas[posicao+3:]
        media2 = notas[posicao+2:]
        return media2