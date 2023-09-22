def acima_da_media(lista_notas):
    media=int(sum(lista_notas)/len(lista_notas))
    if media not in lista_notas:
        list.append(lista_notas,media)
    	list.sort(lista_notas)
    else:
        list.sort(lista_notas)
    return lista_notas[list.index(lista_notas,media)+1:]