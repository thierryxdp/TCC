def acima_da_media(notas):
    soma=sum(notas)
    num=len(notas)
    media=int((soma/num)+1)
    list.append(notas,media)
    list.sort(notas)
    ordem_media=notas.index(media)
    return notas[ordem_media+1:]