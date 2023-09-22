def acima_da_media(lista: list) -> list:
    
    list.sort(lista)
    a = sum(lista)//len(lista)
    
    list.append(lista, a)
    list.sort(lista)
    del lista[:a+1]
    
  

    return lista