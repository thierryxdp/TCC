def acima_da_media(notas):
    media=(sum(notas))/(len(notas))
    if list.count(notas,media)==0:
        list.append(notas,media)
        list.sort(notas)
        pos_med=list.index(notas,media)
        del notas[0:pos_med+1]
        return notas
    
    elif list.count(notas,media)==1:
        list.append(notas,media)
        list.sort(notas)
        pos_med=list.index(notas,media)
        del notas[0:pos_med+2]
        return notas