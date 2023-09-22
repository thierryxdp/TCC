def acima_da_media(notas):
    soma_notas = 0
    media_lista = list()
    
    media = sum(notas[0])/len(notas[0])
    for n in notas[0]:
        if n>=media:
            media_lista.append(n)

    return media_lista