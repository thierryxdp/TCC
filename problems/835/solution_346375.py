def melhor_volta():
    menos = []
    for i in range(len(matriz)):
        menos.append(min(matriz[i]))
        menor = min(menos)
        
        if menor in matriz[i]:
            quem = matriz.index(matriz[i])+1
            qual = matriz[i].index(min(menos))+1
            
    return (quem, menor, qual)