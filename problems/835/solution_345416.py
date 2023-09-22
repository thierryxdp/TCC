def melhor_volta (matriz):
    tempo_minimo_individual = []
    
    for i in range(6):
        tempo_minimo_individual.append(min(matriz[i]))
    tempo_base = tempo_minimo_individual[0]
    corredor_base = 1
    
    for corredor, tempo in enumerate(tempo_minimo_individual):
        if tempo < tempo_base:
            tempo_base = tempo
            corredor_base = corredor
    responsavel_melhor_volta = corredor_base
    melhor_tempo = tempo_base
    
    for volta, tempo in enumerate(matriz[responsavel_melhor_volta]):
        if tempo == melhor_tempo:
            volta_referente = volta
            
    return (responsavel_melhor_volta + 1, melhor_tempo, volta_referente + 1)