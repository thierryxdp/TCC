def melhor_volta(matriz):
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    
    menor_tempo=min(menor)
    
    corredor=menor.index(menor_tempo)
    
    min_matriz_corredor = min(matriz[corredor])
    
    volta_linha=matriz[corredor]
    volta_min=min(volta_linha)
    volta=volta_linha.index(volta_min)
    
    return (corredor+1,menor_tempo,volta+1)