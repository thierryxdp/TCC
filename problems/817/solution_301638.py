def acima_da_media(lista):
    """ retorna a lista acima da media
    lista -> lista """
    media = sum(lista)/len(lista)
    contagem = 0
    while contagem <= len(lista):
        if lista[contagem] <= media :
            del lista[contagem]
            contagem = contagem + 1
            print (lista)
    else:
        return lista