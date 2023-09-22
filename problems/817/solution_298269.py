def acima_da_media(lista):
    
    """Dada uma lista com as notas dos alunos, retorna
    as que ficaram acima da média. list -> list  """
    
    media = sum(lista)/len(lista)
    if media not in lista:
        list.append(lista, media)

    list.sort(lista)
    indice = list.index(lista, media)
    lista2 = lista[indice+1:]
    return lista2