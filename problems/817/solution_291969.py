def acima_da_media(notas):
    media = sum(notas)//len(notas)
    insere = list.append(notas,media)
    ordena_int = list.sort(notas)
    posicao = list.index(notas,media)
    remove_elemento = list.remove(notas,media)
    return notas[posicao:]