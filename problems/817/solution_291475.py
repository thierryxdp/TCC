def acima_da_media(lista):
    list.sort(lista)
    lista2=[]
    a=sum(lista)
    b=len(lista)
    med=a/b
    for i in range(0, b):
        if(lista[i]>med):
            list.append(lista2, lista[i])
    return lista2