def melhor_volta(matriz):
    
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    
    menor_tempo=min(menor)
    
    corredor=menor.index(menor_tempo)
    
    min_matriz_corredor = min(matriz[corredor])
    
    volta=menor.index(menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)