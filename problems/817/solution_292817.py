def acima_da_media(notas):
    media = sum(notas)/len(notas)
    
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(notas[i])
    
    
    for i in range(len(acima)):
        for j in range(len(acima)):
            if acima[i] > acima[j] and i < j: # itera por todos pares de valores e troca as posições se o maior está à esquerda
                temp = acima[j] # para guardar o valor de acima[j]
                acima[j] = acima[i] # trocando o valor de j pelo de i
                acima[i] = temp # trocando o valor de i pelo de j
        
    
    return acima