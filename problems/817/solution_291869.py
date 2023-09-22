def acima_da_media (lista):
    media= sum (lista)/ len(lista)
    mediaint= int (media)
    if mediaint in lista:
        list.remove(lista,mediaint)
   	lista1= lista+ [mediaint]
    list.sort(lista1)
    num = list.index(lista1, mediaint)
    del acima [0:num+1]
   	return lista1