def acima_da_media (lista):
    
    lista = list.sort(lista)
    lista = list.remove(lista,sum(lista)/len(lista))
    
    return lista