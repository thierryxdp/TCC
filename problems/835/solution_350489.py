def melhor_volta(matriz):
    """ Função que recebe como entrada um matriz 6x10
        representando os tempos em segundos de cada 
        volta que cada um dos 6 corredores de uma 
        pista de Kart (que permite 10 voltas para 
        cada corredor) fizeram. A função retorna 
        uma tupla informando: de quem foi a 
        melhor volta da prova, com qual 
        tempo e em que volta;
        list[list] -> tuple"""
    menores_tempos = []
    for i in range(len(matriz)):
        menores_tempos = menores_tempos + [min(matriz[i])]
        for j in range(len(matriz[0])):
            menor_tempo = min(menores_tempos)
            if matriz[i][j] == menor_tempo:
                corredor = i + 1
                tempo = matriz[i][j]
                volta = j + 1
    return (corredor,tempo,volta)