def acima_da_media(notas):
    soma=sum(notas)
    media=soma/len(notas)
    list.sort(notas)
    p=list.index(notas,media)
    acima=notas[p+1:]
    return acima