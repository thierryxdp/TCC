def acima_da_media(notas):
    '''retorna as notas que ficaram acima da média'''
    media=sum(notas)/len(notas)
    if media in notas:
        notas.sort()
        ind=notas.index(media)
        return notas.index[ind+1:]
    else:
        notas.insert(0,media)
        notas.sort()
        ind=notas.index(media)
        return notas[ind+1:]