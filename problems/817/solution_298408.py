def acima_da_media(lista):
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    elif media in lista:
        lista2=sorted(lista)
        return lista2[list.index(lista2,media):len(lista2)]