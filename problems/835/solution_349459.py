def melhor_volta(matriz):
    z=()
    for i in matriz:
        z=min(i)+z
    melhor_tempo=min(z)
    for i in matriz:
        if melhor_tempo in i:
            corredor=i