def melhor_volta(m):
    """Essa função retorna de quem foi a melhor volta, o tempo e qual volta foi
    lista->tupla"""
    
    melhor_tempo = m[0][0]
    
    for i in range(len(m)):
        tempo_corredor = min(m[i])
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i
    
    volta = list.index(m[melhor_corredor],melhor_tempo)
    
    return (melhor_corredor +1,melhor_tempo,volta+1)