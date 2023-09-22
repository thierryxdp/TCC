def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    if media in lista:
        return lista[list.index(lista,media):len(lista)]