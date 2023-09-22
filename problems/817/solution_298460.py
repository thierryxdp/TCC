def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    if media in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,media):len(lista1)]
    elif media not in lista:
        list.insert(lista,1,media)
        lista2=sorted(lista)
        return lista2[list.index(lista2,media)+1:len(lista2)]