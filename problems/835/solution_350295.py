def melhor_volta(matriz):
    tempo=()
    for i in matriz:
        for j in i:
            tempo+=(j,)
    btempo= min(tempo)
    
    return btempo