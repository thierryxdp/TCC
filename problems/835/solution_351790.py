def melhor_volta(matriz):
    
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    
    menor_tempo=min(menor)
    
    corredor=menor.index(menor_tempo)
    
    volta=matriz.index(88)
    
    return (corredor+1,menor_tempo,volta+1)