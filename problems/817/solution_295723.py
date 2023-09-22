def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = (sum(notas))//len(notas)
    adicionar = list.append (notas,int(media))
    list.sort(notas)
    posicao = list.index(notas, media)
    media2 = notas[-posicao:]
    media3 = notas[posicao+2:]
    if media <= 5:
        return media2
    
    if media >5:
        return media3