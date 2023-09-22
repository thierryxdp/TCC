def acima_da_media(lista):
   
    media= sum(lista)/len(lista)
    if media in lista:
        l1=x(lista,media)
        list.remove(l1,media)
        l2=l1
        return l2
    else:
        
        l3=x(lista,media)
        return l3