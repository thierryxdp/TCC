def acima_da_media(notas: list[float]) -> list[float]:
    '''Retorna as notas que estão acima da média'''
    media = sum(notas)/len(notas)
    acimaDaMedia = maiores(notas, media, True)
    return acimaDaMedia