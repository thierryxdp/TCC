def acima_da_media(notas):
    numero_de_notas = len(notas)
    soma_das_notas = sum(notas)
    media = (soma_das_notas/numero_de_notas)
    lista = []
    if notas[0:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[0])
    else:
        lista = lista
    if notas[1:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[1])
    else:
        lista = lista
    if notas[2:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[2])
    else:
        lista = lista
    if notas[3:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[3])
    else:
        lista = lista
    if notas[4:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[4])
    else:
        lista = lista
    if notas[5:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[5])
    else:
        lista = lista
    if notas[6:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[6])
    else:
        lista = lista
    if notas[7:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[7])
    else:
        lista = lista
    if notas[8:numero_de_notas+1:100] > [media]:
        list.append(lista,notas[8])
    else:
        lista = lista
    lista.sort()
    return lista