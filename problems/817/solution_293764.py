def acima_da_media(lista: list) -> list:
    
    list.sort(acima_da_media)
    
    list.append(lista, sum(lista)/len(lista))
    
    return acima_da_media