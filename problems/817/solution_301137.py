def acima_da_media(lista):
    '''Função que verifica a lista de entrada, e identifica as notas maiores que a media e por fim
    retorna uma lista com essas notas.
    list,list→list'''
    lista_medias=[]
    for i in lista:
        if i > 4:
            lista_medias.append(i)
            lista_medias.sort()    
	return lista_medias