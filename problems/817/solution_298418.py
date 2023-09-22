def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    if n in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,n):len(lista1)]
    elif n not in lista:
        list.insert(lista,1,n)
        lista2=sorted(lista)
        return lista2[list.index(lista2,n)+1:len(lista2)]