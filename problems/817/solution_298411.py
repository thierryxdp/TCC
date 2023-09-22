def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    elif media in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,media):len(lista1)]