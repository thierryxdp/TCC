def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    media = sum(lista)//len(lista)
    if media in lista:
        lista.sort()
        indice = lista.index(media)
        return lista[int(indice+1):]
    elif media not in lista:
        lista.insert(media,media)
        lista.sort()
        lista.remove(media)
        return lista[int(indice+1):]