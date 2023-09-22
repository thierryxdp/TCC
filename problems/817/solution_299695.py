def acima_da_media(lista_notas:list)->list:
    """Dada uma lista ordenada de números int, inclui n na posição correta, de forma que a lista contuinue ordenada."""
    media = sum(lista_notas)/len(lista_notas)
    lista_notas.append(media)
    lista_notas.sort()
    num = lista_notas.index(media)
    del lista_notas[0:num+1]
    if len(lista_notas)==1:
        return []
    else:
        return lista_notas