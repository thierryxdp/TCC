def acima_da_media(lista):
    tamanho_lista = len(lista)
    media = round(sum(lista)/tamanho_lista,0)
    lista.append(media)
    lista.sort()
    posicao = lista.index(media)
    return lista[posicao+1:tamanho_lista+1]