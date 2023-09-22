def acima_da_media(lista):
    """Retorna uma lista ordenada com as notas que ficaram acima da média.
    lista --> lista"""
    
    media = sum(lista)/len(lista)
    
    index = list.index(lista,media) + 1
    
    nova_lista = lista[index:]
    
    return nova_lista