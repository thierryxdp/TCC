def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    media=int(sum(notas)/len(notas))
    notas.append(media)
    x=notas.index(media)
    list.sort(notas)
    return x