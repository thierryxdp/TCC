def acima_da_media (lista):
    media= sum (lista)/ len(lista)
    mediaint= int (media)
    if mediaint in lista:
        list.remove(lista,mediaint)
   	acima= lista+ [mediaint]
    list.sort(acima)
    num = list.index(acima, mediaint)
    del acima [:num+1]
   	return acima