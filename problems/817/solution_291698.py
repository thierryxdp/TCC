def acima_da_media(lista):
    #retorna uma lista com notas maiores que a media.
    #list - list
    maiores=[]
    media=0
    for i in range(len(lista)):
        media+=lista[i]
    media=media/len(lista)
    for i in range(len(lista)):
        if lista[i]>media:
            maiores.append(lista[i])
        else:
            continue
    maiores.sort()
    return maiores