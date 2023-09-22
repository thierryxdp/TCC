def acima_da_media(notas):
    lista_notas = []
    lista_vazia = []
    if len(acima_da_media) < 1:
        return lista_vazia
    for e in notas:
        if e >= 5:
            lista_notas.append(e)
	lista_notas.sort()
    return lista_notas