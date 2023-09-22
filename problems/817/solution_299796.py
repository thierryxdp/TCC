def acima_da_media (lista):
    '''
    funçao que dada uma lista com as notas dos alunos, retorne
    uma lista somente com as notas que foram acima da media
    list -> list
    '''
    media = round((sum(lista)/int(len(lista))),1)
    lista2 = [media]
    lista3 = lista+lista2
    list.sort(lista3)
    numero = int(lista3.index(media))
    if media in lista3:
        return lista3[(numero+2)::]
    else:
    	return lista3[(numero+1)::]