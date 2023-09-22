def inverte(lista):
    lista= str.lower(lista)
    lista=lista[0:-1]
    lista=str.replace(lista, ",","")
    lista=str.replace(lista,"-"," ")
    lista=str.split(lsita,)
    list=lista
    list.reverse()
    a= str.join(" ", list)
    return a