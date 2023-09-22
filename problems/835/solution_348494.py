def melhor_volta(matriz):
    '''
    Função que recebe como entrada uma matriz com os tempos
    em segundos dos corredores em cada volta de uma corrida
    e retorna de quem foi a melhor volta da prova, o tempo
    e a volta.
    
    list -> int, int, int
    '''
    voltas = []
    for corredor in matriz:
        voltas.append(min(corredor))
    melhor = min(voltas)
    corredor = voltas.index(melhor)
    volta = matriz[corredor].index(melhor)
    return corredor+1, melhor, volta+1