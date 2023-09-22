def acima_da_media(lista):
    media=(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    ps=list.index(lista,media)
    repeticao=list.count(lista,media)
    x=1+repeticao
    lista1=lista[ps+x:]
    return lista1