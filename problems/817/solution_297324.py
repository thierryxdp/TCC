def acima_da_media(notas):
    '''
    '''
    
    media = sum(notas)/len(notas)
    list.append(notas, media)
	list.sort(notas)
    posicao = int((list.index(notas, media))
    del notas[:posicao + 1]
    return(notas)