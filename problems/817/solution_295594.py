def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = int(sum(notas))//len(notas)
    adicionar = list.append (notas,media)
    list.sort(notas)
    posicao = list.index(notas, media)
    media2 = notas[posicao+2:]
    media3 = notas[posicao+2:]
    if int (media) >= (sum(notas)):
        return (sum(notas))
    else:
        return media2