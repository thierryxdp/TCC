def acima_da_media (lista):
    media= sum (lista)/ len(lista)
    mediaint= int (media)
   	acima= lista+ [mediaint]
    list.sort(acima)
    num = list.index(acima, mediaint)
    del acima [:num]
   	return acima