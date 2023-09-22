def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da media'''
    media= sum(notas)/len(notas)
    notas.sort()
    b= del notas[:media+1]
    return b