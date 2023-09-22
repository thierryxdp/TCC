def acima_da_media(lista_notas):
    '''funcao que retorna uma media dada
    uma lista com notas
    entrada: lista
    saida: lita
    '''
    media= sum(lista_notas)/len(lista_notas)
    if media in lista_notas:
        list.sort(lista_notas)
        posicao= list.index(lista_notas,media)
        return lista_notas[(posicao+1):]
    else:
    	list.insert(lista_notas,0,media)
    	list.sort(lista_notas)
    	posicao= list.index(lista_notas,media)
    	return lista_notas[(posicao+1):]