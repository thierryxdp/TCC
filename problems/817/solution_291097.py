def acima_da_media(lista):
   
    media= sum(lista)/len(lista)
    
    if media in lista:
        l1=maior
        maior=(lista,media)
        list.remove(maior,media)
        l2=maior
        return l2
    else:
        
        l3=maior(lista,media)
        return l3