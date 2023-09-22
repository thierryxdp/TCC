def  acima_da_media(lista):
    '''descricao'''
    media=sum(lista)/round(len(lista))
    list.append(lista, media)
    list.sort(lista)
    media_e_acima=lista[list.index(lista,media)+1:]
	return media_e_acima