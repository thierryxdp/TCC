def acima_da_media(lista):
    ordem=lista
    list.sort(ordem)
    if (len(ordem)%2) == 0:
        return ordem[(len(ordem)//2):]
    else:
        return ordem[((len(ordem)//2)+1):]