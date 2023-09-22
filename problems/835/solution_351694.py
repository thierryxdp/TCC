def melhor_volta(matriz):
    
    menor = []
    for linha in matriz:
        menor.append(min(linha))
    menor_tempo=min(menor)
    corredor=menor_tempo.index(menor,menor_tempo)
    volta=list.index(matriz,corredor)
    return (corredor+1,volta+1)