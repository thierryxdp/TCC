def acima_da_media(notas):
    lista_notas = []
    media = sum(notas) / 2
    for e in notas:
        if e >= media:
            lista_notas.append(e)
	lista_notas.sort()
    return lista_notas