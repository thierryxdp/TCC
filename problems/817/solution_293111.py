def acima_da_media(lista):
    '''Dado uma lista com as notas dos alunos de uma turma, retorna uma 
    lista ordenada com as notas que ficaram acima da media.
    list -> list'''
    media=(sum(lista)/len(lista))
    media=media
    lista=lista+[media]
    lista2=lista[:]
    list.sort(lista)
    indice=list.index(lista,media)
    if (media) in lista2:
        return lista[indice+2:]