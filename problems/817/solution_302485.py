def acima_da_media(notas):
    lista=[]
    media=sum(notas/(len(notas)))
    for i in lista:
        if i>media:
            lista.append(i)
     return list.sort(lista)