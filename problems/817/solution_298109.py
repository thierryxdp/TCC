def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    list.sort(notas)
    media=int(sum(notas)/len(notas))
    media=notas.index(media)
    return notas[media:]