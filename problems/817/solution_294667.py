def acima_da_media(notas):
    """ """
    soma=sum(notas)
    quant=len(notas)
    media=(soma/quant)
    ordenada=list.sort(notas)
    return list.index(ordenada,media)