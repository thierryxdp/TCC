def acima_da_media(notas):
    ''' Função que recebe uma lista contendo notas, 
    e retorna todas as notas acima da média
    list -> list '''
    
    if len(notas) == 1:
        return []
    elif len(notas) ==2 and notas[:1] ==0:
        return notas[1:]
    elif len(notas) ==2 and nota[1:] == 0:
        return notas[:1]
    
    media = (sum(notas)/len(notas))
    list.appen(notas,media)
    list.sort(notas)
    notas[list.index(notas,media):]
    acima = notas[list.index(notas,media):]
    list.remove(acima,media)
    return acima