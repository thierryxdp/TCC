def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    media=int(sum(notas)/len(notas))
    notas.append(media)
    list.sort(notas)
    x=notas.index(media)
    
    return notas[x:]