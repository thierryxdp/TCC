def acima_da_media(lista: list) -> list:
    
    list.sort(lista)
    
    list.append(lista, sum(lista)/len(lista))
  

    return acima_da_media