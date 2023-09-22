def melhor_volta(matriz):
    """ Função que recebe como entrada um matriz 6x10
        representando os tempos em segundos de cada 
        volta que cada um dos 6 corredores de uma 
        pista de Kart (que permite 10 voltas para 
        cada corredor) fizeram. A função retorna 
        uma tupla informando: de quem foi a 
        melhor volta da prova, com qual 
        tempo e em que volta;
        list(list) -> tuple"""
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i] == min(matriz) and matriz[i][j] == min(matriz[i]):
                tempo = matriz[i][j]
                corredor = i
                volta = j
    return (corredor,tempo,volta)