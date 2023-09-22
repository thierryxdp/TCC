def acima_da_media(notas):
    """ """
    soma=sum(notas)
    quant=len(notas)
    media=int(soma/quant)+
    ordenada=list.sort(notas)
    x= list.index(ordenada,media)
    return x