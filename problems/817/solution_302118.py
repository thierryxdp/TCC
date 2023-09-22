def acima_da_media(lista):
    l_final = []
    media = 5
    for i in lista:
        if i >= media:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final