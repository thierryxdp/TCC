def acima_da_media(notas):
    '''Retorna, ordenadamente, as notas acima da média da lista com notas dada; list[float] -> list[float]'''
	media=sum(notas)/len(notas)
    media=round(media)
    if media not in notas:
        list.append(notas, media)
        list.sort(notas)
        return notas[media+1:]
    list.sort(notas)
    return notas[media+1:]