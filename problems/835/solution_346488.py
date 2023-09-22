def melhor_volta(matriz):
    lista = []
    for i in range(len(matriz)):
        lista.append(min(matriz[i]))
        menor_tempo = min(lista)
        
        if menor_tempo in matriz[i]:
            corredor = matriz.index(matriz[i])+1
            volta = matriz[i].index(min(lista))+1
            
    return (corredor, menor_tempo, volta)