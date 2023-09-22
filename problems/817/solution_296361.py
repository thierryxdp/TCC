def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da média.'''
    media = sum(notas)/len(notas)  
    
    notasCopia = notas.copy()
    notasCopia.append(media)
    notasCopia.sort()
    posicaoMedia = notasCopia.index(media)
    maiores = notasCopia[media+1:]
    
    acimaMedia = maiores(notas, media, True)
    return acimaMedia