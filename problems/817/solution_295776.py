def maiores(lista_numero,n):
    lista=lista_numero
    list.append(lista,n)
    lista_com_n=lista
    list.sort(lista_com_n)
    total_elementos=len(lista_com_n)
    posicao_n=list.index(lista_com_n,n)
    if posicao_n==(total_elementos-1):
        list.clear(lista_com_n)
        return lista_com_n
    elif 0<posicao_n<(total_elementos-1):
        if list.count(lista_com_n,n)==2:
            list.remove(lista_com_n,n)
            return lista_com_n[posicao_n+1:]
        else:
            return lista_com_n[posicao_n+1:]
    
def acima_da_media(lista_medias):
    if len(lista_medias)>1:
        media= sum(lista_medias)//(len(lista_medias)-1)
        lista_acima_da_media= maiores(lista_medias,media)
        return lista_acima_da_media
    else:
        list.clear(lista_medias)
        return lista_medias