def acima_da_media(notas):
    '''list->list que retorna as notas acima da media'''
    media=(sum(notas)/len(notas))
    list.sort(notas)
    pos=list.index(notas,media)
    del notas[0:pos+1]
    return notas