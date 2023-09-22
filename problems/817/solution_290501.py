def acima_da_media(lista):
    media = sum(lista)/len(lista)
    nova_lista = list()
    for i in lista:
        if i > media:
            list.extend(nova_lista,[i])
    return(nova_lista)