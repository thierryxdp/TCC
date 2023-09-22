def acima_da_media (lista):
    media= sum (lista)/ len (lista)
    media_int= int (media)
    if media_int in lista:
        list.remove(lista,media_int)
  	lista_1= lista+ [media_int]
    list.sort(lista_1)
    num= list.index(lista_1, media_int)
    del lista_1 [:num+1]
    return lista_1