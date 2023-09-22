def acima_da_media(notas):
    media = sum(notas)/len(notas)
    
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(notas[i])
    
    acima_ord = [1]
    
    for i in range(len(acima)):
        for j in range(len(acima_ord)):
            if acima[i] >= acima[j]:
                acima_ord.append(acima[i])
               		
        
    
    return acima_ord