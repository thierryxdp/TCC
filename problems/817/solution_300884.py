def acima_da_media (lista_com_notas):
    
    media = sum(lista_com_notas)/ len(lista_com_notas)
    if media not in lista_com_notas:
        lista_com_notas.insert(0, media)
        
    lista_com_notas.sort()
    ind = lista_com_notas.index(media)
    
    return lista_com_notas[ind+1:]