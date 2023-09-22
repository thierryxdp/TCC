def acima_da_media(notas):
    soma=sum(notas)
    divisor=len(notas)
    media=soma/divisor
    notas.append(media)
    notas.sort()
    indice=list.index(notas,media)
    return notas[indice+2:]