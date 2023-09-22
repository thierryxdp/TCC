def acima_da_media(lista):
    '''funcao que pega a lista de aluno e a media deles e organiza'''
    med = (sum(lista)/len(lista))
    medias = []
    for i in lista:
        if i>med:
            medias.append(i)
    return(sorted(medias))