def acima_da_media(notas, media):
    lista_notas = []
    for e in notas:
        if e >= media:
            lista_notas.append(e)
	lista_notas.sort()
    return lista_notas