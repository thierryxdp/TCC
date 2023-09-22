def melhor_volta(matriz):
    '''Retorna uma tupla informando o corredor, o tempo da volta e o numero da volta da melhor volta em um circuito de Kart'''
    #list -> tuple
    volta = []
    melhor_tempo = []
    for linha in matriz:
        n_volta = 1
        for Aij in linha:
            if Aij == min(linha):
                list.append(melhor_tempo, Aij)
                list.append(volta, n_volta)
            n_volta = n_volta + 1
    corredor = 1
    for tempo in melhor_tempo:
        if tempo == min(melhor_tempo):
            return (corredor, tempo, volta[corredor])
        corredor = corredor + 1