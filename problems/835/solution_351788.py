def melhor_volta(matriz):
    
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    
    menor_tempo=min(menor)
    
    corredor=menor.index(menor_tempo)
    
    volta=matriz.index(corredor)
    
    return (corredor+1,volta+1)