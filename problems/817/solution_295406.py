def acima_da_media(notas):
    list.sort(notas)
    media = sum(notas)//len(notas)
    return notas[media:]