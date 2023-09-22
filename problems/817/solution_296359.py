def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da média.'''
    media = sum(notas)/len(notas)
    acimaMedia = max(notas, media, True)
    return acimaMedia