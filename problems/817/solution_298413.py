def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    if media in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,media):len(lista1)]