def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da media'''
    media= sum(notas)/len(notas)
    notas.sort()
    del notas[:media+1]
    return notas