def acima_da_media(notas)
    media=(notas.sum())/len(notas)
    notas.sort()
    return notas[media:]