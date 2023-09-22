def melhor_volta(matriz):
    '''Ao fornecer uma matriz 6x10 que representa o tempo 6 corredores em 10 voltas,
    retorne um tupla com o corredor que obteve o melhor tempo, qual foi o melhor tempo
    e por fim em qual volta obteve-se o melhor resultado.

    list -> tuple'''
    
    tempo = []
    volta = []
    for i in range(len(matriz)):
        list.append(tempo, min(matriz[i]))
        for j in range(len(matriz[0])):
            if (matriz[i][j] == min(matriz[i])):
                list.append(volta,matriz[i].index(matriz[i][j]))
            
    return (tempo.index(min(tempo))+1,min(tempo),volta[list.index(tempo,min(tempo))]+1)