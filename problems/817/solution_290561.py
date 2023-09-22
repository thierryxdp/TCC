def acima_da_media(notas):
    media=(sum(notas))/(len(notas))
    list.append(notas,media)
    list.sort(notas)
    pos_med=list.index(notas,media)
    del notas[0:pos_med+1]
    return notas