def acima_da_media(lista):
    ''' devolve as notas que ficaram acima da media '''
    media=sum(lista)//len(lista)
    acima_media=lista[:]>media
    return list.sort(acima_media)