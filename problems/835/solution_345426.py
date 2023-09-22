def melhor_volta (matriz):
    '''Retorna o número do piloto que fez a volta mais rápida da prova, o seu tempo de volta e o número da volta em questão
    em base de uma matriz 6x10 inserida inicialmente com o tempo em segundos dos corredores em cada volta;
    list -> tuple'''
    tempo_minimo_individual = []
    volta_referente = 0
    
    for i in range(6):
        tempo_minimo_individual.append(min(matriz[i]))
    tempo_base = tempo_minimo_individual[0]
    piloto_base = 0
    
    for piloto, tempo in enumerate(tempo_minimo_individual):
        if tempo < tempo_base:
            tempo_base = tempo
            piloto_base = piloto
    responsavel_melhor_volta = piloto_base
    melhor_tempo = tempo_base
    
    for volta, tempo in enumerate(matriz[responsavel_melhor_volta]):
        if tempo == melhor_tempo:
            volta_referente = volta
            
    return (responsavel_melhor_volta + 1, melhor_tempo, volta_referente + 1)