def acima_da_media(lista):
    list.sort(lista)
    copia = []
    media = sum(lista)/len(lista)
    
    for i in lista:
        if(i > media):
            copia.append(i)

    return copia