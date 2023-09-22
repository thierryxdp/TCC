def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas)
    acimaDaMedia = maiores(notas,media,True)
    return acimaDaMedia