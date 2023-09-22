def acima_da_media(notas):
    lista_notas = []
    lista_vazia = []
    media = (sum(notas) / len(notas))
    if len(notas) == 1:
        return lista_vazia
    else:
    	for e in notas:
        	if e >= media:
            	lista_notas.append(e)
	lista_notas.sort()
    return lista_notas