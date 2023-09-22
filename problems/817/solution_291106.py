def acima_da_media(lista):
    
    media= sum(lista)/len(lista)
    
    if media in lista:
        A = maior(lista,media)
        list.remove(l1,media)
        B=A
        return B
    else:
        C= maior(lista,media)
        return C