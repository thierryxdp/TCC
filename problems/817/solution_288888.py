def acima_da_media(notas):
    soma_notas = 0
    media_lista = list()
    for c in notas[0]:
        soma_notas = soma_notas + c
    media = soma_notas/len(notas[0])
    for c in notas[0]:
        if(c>=media):
            media_lista.append(c)

    return media_lista