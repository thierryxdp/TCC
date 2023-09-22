def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    list.sort(notas)
    media=int(sum(notas)/len(notas))
    return notas[media:]