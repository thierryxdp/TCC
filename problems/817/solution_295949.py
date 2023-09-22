def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = (sum(notas))/len(notas)
    list.append (notas,(media))
    list.sort(notas)
    if media not in notas:
        posicao = list.index(notas, media)
        final= notas[posicao+1:]
        return final
    else:
        return notas[posicao+1:]