def acima_da_media(notas):
    
    media = int(sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    com_media = list.index(notas,media)
    acima = notas [com_media:]
    
    return acima