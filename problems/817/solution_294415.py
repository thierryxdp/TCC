def acima_da_media(lista):
    media=(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    ps=list.index(lista,media)
    repeticao=list.count(lista,media)
    if repeticao==1:
    	lista1=lista[ps+1:]
    	return lista1
    else:
        x=repeticao-1
        lista2=lista[ps+1+x:]
        return lista2