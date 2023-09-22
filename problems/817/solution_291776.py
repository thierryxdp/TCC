def acima_da_media():
    media=(notas.sum())/len(notas)
    notas.sort()
    return notas[media:]