def acima_da_media(notas):
    """ Retorna uma lista com as notas acima da média dentro da lista notas; list->list """
    media=sum(notas)/len(notas);
    list.append(notas,media);
    list.sort(notas);
    if (list.count(notas,media)==1):
        return notas[list.index(notas,media)+1:];
    else:
        if(list.count(notas,media)>=2):
            return notas[list.index(notas,media)+list.count(notas,media):];