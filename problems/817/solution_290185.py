def acima_da_media(lista):
    '''Calcula e retorna uma lista, a partir de uma lista original, com os elementos da lista original que sejam maiores que a media da propria lista
       parameters:
       lista: lista com numeros
       list->list'''
    media=sum(lista)/len(lista)
    if media in lista:
        lista.append(media)
        lista.sort()
        posicao=lista.index(media)
        return lista[posicao+2:]
    else:
        lista.append(media)
        lista.sort()
        posicao=lista.index(media)
        return lista[posicao+1:]