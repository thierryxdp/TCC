def acima_da_media (lista):
    media = sum(lista)/len(lista)
    
    lista.append(media)
    lista.sort()
    posicao= lista.index(media)+1
    
    lista= lista[posicao:]
    
    if media in lista:
        list.remove(lista,media)
        return lista
    else:
        return lista