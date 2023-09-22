def acima_da_media(lista):
    lista2=[]
    for i in lista:
        if i > ((sum(lista))/len(lista)):
            lista2.append(i)
            list.sort(lista2)
    return lista2