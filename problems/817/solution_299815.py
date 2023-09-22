def acima_da_media (lista):
    '''lista ordenada com as notas acima da media'''
    media = int(sum(lista)/ len(lista))
    lista.append(media)
    listaOrg = sorted(lista)
    indmedia = listaOrg.index(media)
    novaLista = listaOrg[indmedia + 1:]
    if media in novaLista:
        del novaLista[0]
    return novaLista