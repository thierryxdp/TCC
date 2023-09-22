def acima_da_media(lista):

    list.sort(lista)

    media = sum(lista)/ (list.index(lista,lista[-1]) + 1)

    media = int(media)

    list.append(lista,media)

    list.sort(lista)

    x = list.index(lista,media)

    lista = lista[x:]

    if lista[0]==lista[1]:
        
        del lista[0]
        
        del lista[0]
        
        return lista

    else:
        
        del lista[0]
        
        return lista