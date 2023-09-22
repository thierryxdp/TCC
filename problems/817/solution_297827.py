def acima_da_media(nota):
    """primeiro fazemos descobrimos a media das notas, depois acrescentamos
    na lista nota, ordenamos a lista, e localizamos a posicao do valor da media
    depois retornamos apenas as notas maiores que o valor da media
    list -> list"""
    media=sum(nota)/len(nota)
    lista=nota+[media]
    lista.sort()
    x=lista.index(media)
    return lista[x+1:]