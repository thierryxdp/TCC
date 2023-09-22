def acima_da_media(notas):
    lista_notas = []
    for e in notas:
        if e >= 5:
            lista_notas.append(e)
	lista_notas.sort()
    return lista_notas