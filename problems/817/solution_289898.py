def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média
    list->list'''
    media=sum(lista)/len(lista)
    x=lista > media
 	return x