def acima_da_media(notas):
    '''retorna uma lista ordenada com somente as notas dos alunos que são maiores que a media dentre elas
    list -> list'''
    media = sum(notas)/len(notas)
    if media not in notas:
        list.append(notas,media)
        list.sort(notas)
        posicao = list.index(notas,media)
        return notas[posicao+1:]
    else:
        list.sort(notas)
        posicao = list.index(notas,media)
        return notas[posicao+1:]