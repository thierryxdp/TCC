def acima_da_media(notas):
    media = sum(notas)/len(notas)
    
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(notas[i])
    
    
    for i in range(len(acima)):
        for j in range(len(acima)):
            if acima[i] > acima[j] and i > j:
                temp = acima[j]
                acima[j] = acima[i]
        
    
    return acima