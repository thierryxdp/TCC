def melhor_volta(matriz):
    corredores= len(matriz)
    voltas= len(matriz[0])

    menor_tempo= [0] [0]
    for voltas in range(corredores):
        for tempo in range(voltas):
            if menor_tempo>=matriz[voltas][tempo]:
                menor_tempo=matriz[voltas] [tempo]

                melhor_corredor = volta+1
                qual_volta = tempo+1

    return(melhor_corredor, menor_tempo, qual_volta)