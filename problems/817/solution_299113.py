def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da media'''
    media= sum(notas)/len(notas)
    notas.sort()
    return notas[notas.index(media)+1:]