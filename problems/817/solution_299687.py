def acima_da_media(lista_notas:list)->list:
    """Dada uma lista ordenada de números int, inclui n na posição correta, de forma que a lista contuinue ordenada."""
    lista_notas.sort()
    media = sum(lista_notas)/len(lista_notas)
    lista_numero.append(media)
    num = lista_notas.index(media)
    del lista_notas[0:num+1]
    return lista_notas