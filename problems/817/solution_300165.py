def acima_da_media(notas):
    '''retorna as notas que ficaram acima da média'''
    if 5 in notas:
        notas.sort()
        ind=notas.index(5)
        return notas.index[ind:]
    else:
        notas.insert(0,5)
        notas.sort()
        ind=notas.index(5)
        return notas[ind+1:]