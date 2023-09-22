def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    media=sum(notas)/len(notas)
    list.sort(notas)
    x=notas.index(media)
    return notas[x+1:]