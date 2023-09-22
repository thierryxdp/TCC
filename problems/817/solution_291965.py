def acima_da_media(notas):
    media = sum(notas)//len(notas)
    numero = media
    insere = list.append(notas,numero)
    ordena_int = list.sort(notas)
    posicao = list.index(notas,numero)
    return notas[posicao+1:]