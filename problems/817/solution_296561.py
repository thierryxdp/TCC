def acima_da_media(notas):
    lista_nova = []
    lista_nova1 = notas[:]
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    ind_n = list.index(notas,media)
    if media in lista_nova1:
        return lista[ind+2:]
    elif len(lista)>2:
        return lista[ind+1:]
    else:
        return lista_nova