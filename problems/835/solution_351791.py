def melhor_volta(matriz):
    
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    
    menor_tempo=min(menor)
    
    corredor=menor.index(menor_tempo)
    
    
    
    return (corredor+1,menor_tempo,linha+1)