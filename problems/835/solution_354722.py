def melhor_volta(m):
    corredores= len(m)
    voltas= len(m[0])
    
    menor_tempo=[0][0]
    for voltas in range(corredores):
        for tempo in range(voltas):
            if menor_tempo>=m[voltas][tempo]:
                menor_tempo=m[voltas][tempo]
                melhor_corredor= voltas+1
                qual_volta=tempo+1
    return(melhor_corredor,menor_tempo,qual_volta)