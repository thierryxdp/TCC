def acima_da_media(lista):
    """Retorna uma lista ordenada com as notas que ficaram acima da média.
    lista --> lista"""
    
    
    
    media = (sum(lista)/len(lista)) 
    
    list.append(lista, media)
    
    list.sort(lista)
    
    index = list.index(lista,media) + 1
    
    nova_lista = lista[index:]
    
    if media in nova_lista:
        list.remove(nova_lista,media)
    
    return nova_lista