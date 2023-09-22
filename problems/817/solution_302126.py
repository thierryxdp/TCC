def acima_da_media(lista):
    l_final = []
    for i in lista:
        media = lista/len(lista)
        if i >= media:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final