def melhor_volta(matriz: list)-> tuple:
    '''Retorna de quem foi a melhor volta, qual seu tempo
    e em que volta de uma corrida de Karts'''
    melhor_volta = 0
    tempo = 100000
    corredor = 0
    indice = 1
    for i in matriz:
        if min(i)< tempo:
            tempo=min(i)
            corredor = indice
            melhor_volta= i.index(tempo)+ 1
        indice += 1
    return (corredor, tempo, melhor_volta)