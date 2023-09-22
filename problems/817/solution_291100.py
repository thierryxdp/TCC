def acima_da_media(lista):
    l1 = maiores
    media= sum(lista)/len(lista)
    if media in lista:
        l1= (lista,media)
        list.remove(l1,media)
        l2=l1
        return l2
    else:
        
        l3= maiores(lista,media)
        return l3