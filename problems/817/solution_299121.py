def acima_da_media(notas:list[float])->list[float]:
    '''Retorna as notas acima da media'''
    media= sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    notasMaiores=notas[notas.index(media)+1:]
    
    if media in notasMaiores:
        quantid=notasMaiores.count(media)
        notasMaiores=notasMaiores[quantid:]
    else:
        pass
    
    return notasMaiores