def acima_da_media(lista):
    '''Função que recebe uma lista,calcula a média e retorna uma lista com os números maiores da 
média aritimética '''
    media_lista=sum(lista)/len(lista)
    list.append(lista,media_lista)
    list.sort(lista)
    indice=list.index(lista,media_lista)
    lista1=lista[indice+1:]
    if media_lista not in lista:
        return lista1
    else:
        del lista1[0]
        return lista1