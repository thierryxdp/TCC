def acima_da_media(lista, media=5):
    l_final = []
    
    for i in lista:
        if i >= media:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final