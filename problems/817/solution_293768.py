def acima_da_media(lista: list) -> list:
    
    list.sort(lista)
    a = sum(lista)//len(lista)
    
    list.append(lista, a)
  

    return lista