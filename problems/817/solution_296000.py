def maiores(lista,n):
    ''''''
    lista_com_n = lista+[n]
    list.sort(lista_com_n)
    return lista_com_n[list.index(lista_com_n,n)+1:]

def acima_da_media(notas):
    ''''''
    list.sort(notas)
    media=sum(notas)/len(notas)
    if notas == [media]:
        return[]
    if media in notas:
        listafinal = maiores(notas,media)
        remove(listafinal,media)
    else:
        return maiores(notas,media)