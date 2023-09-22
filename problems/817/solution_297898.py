def acima_da_media(notas):
    
    media = int (sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    acima = notas[list.index(notas,media):]
    list.remove(acima,media)
    
    
    return acima