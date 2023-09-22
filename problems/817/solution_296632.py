def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas)
    acimadamedia = maiores(notas,media,True)
    return acimadamedia