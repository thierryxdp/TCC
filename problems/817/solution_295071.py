def acima_da_media(lista_notas, media):
    cont = 0
    lista2_notas = []
    while cont < len(lista_notas):
        if lista_notas[cont] > media:
            lista2_notas.append(lista_notas[cont])
        cont = cont + 1
    lista2_notas.sort()
    return lista2_notas