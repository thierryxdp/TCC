def acima_da_media(notas):
    media = sum(notas)/len(notas)
    
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(notas[i])
    
    return acima