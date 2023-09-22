def acima_da_media(lista):
    """ Retorna os alunos que ficaram
        acima da média list,int->list"""
    list.sort(lista)
    xtermos = sum(lista)
    ytermos = len(lista)
    media = xtermos//ytermos
    if media in lista:
        v1 = list.index(lista,media)
        p = v1+1
        return lista[p:]
    else:
        list.append(lista,media)
        list.sort(lista)
        v1 = lista.index(lista,media)
        p = v1+1
        return lista