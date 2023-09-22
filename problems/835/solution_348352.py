def melhor_volta(matriz):
    lista=[]

    for i in range(len(matriz)):
        minimo = min(matriz[i])
        lista.append(minimo)
        minimo = min(lista)
        
    for j in range(len(matriz)):
        for k in range(len(matriz[0])):
            if minimo == matriz[j][k]:
                pessoa = j+1
                tempo = matriz[j][k]
                volta = matriz[j].index(matriz[j][k])+1
                    
    return (pessoa,tempo,volta)