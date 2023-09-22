def acima_da_media(lista):
    '''funcao que pega a media dos alunos e organiza'''
    med = (sum(lista)/len(lista))
    medias = []
    for i in lista:
        if i>med:
            medias.append(i)
    return(sorted(medias))