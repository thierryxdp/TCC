def acima_da_media(lista):
    x = sum(lista)/len(lista)
    listi2=[]
    for i in lista:
        if i>x:
            lista2.append(i)
            list.sort(lista2)
    return lista2