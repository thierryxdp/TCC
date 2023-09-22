def melhor_volta(pilotos):
    tempos = []
    for piloto in pilotos:
        menor = min(piloto)
        tempos.append(menor)
    melhor_tempo = min(tempos)
    melhor_piloto = tempos.index(melhor_tempo)
    volta = pilotos[melhor_piloto].index(melhor_tempo)
    
    return (melhor_piloto+1,melhor_tempo,volta+1)