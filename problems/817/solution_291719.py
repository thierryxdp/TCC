def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    media = sum(lista)/len(lista)
    if lista > media:
        lista.insert(media,media)
        lista.sort()
        indice = lista.index(media)
        acimaMedia = lista[indice+1:]  
        acimaMedia.remove(media)
        return acimaMedia
    elif media in lista:
        return acimaMedia