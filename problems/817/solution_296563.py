def acima_da_media(notas):
    lista_nova = []
    lista_nova1 = notas[:]
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    ind_n = list.index(notas,media)
    if media in lista_nova1:
        return notas[ind_n+2:]
    elif len(notas)>2:
        return notas[ind_n+1:]
    else:
        return lista_nova