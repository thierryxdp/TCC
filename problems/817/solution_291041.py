def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    soma=sum(lista)
    média=soma/len(lista)
    
    list.sort(lista)
    list.remove(list[:média])
    return lista