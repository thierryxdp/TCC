def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    media = (sum(notas))//len(notas)
    adicionar = list.append (notas,int(media))
    list.sort(notas)
    posicao = list.index(notas, media)
    if posicao in notas:
        list.remove (notas,posicao-1)
        
    media2 = notas[posicao:]
    media3 = notas[posicao+2]
    teste= list.remove (notas, posicao+1)
    
    return media2