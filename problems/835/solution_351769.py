def melhor_volta(tempos):
    '''funçao que dado os tempos de cada volta em uma corrida,retorne quem foi a melhor volta,qual foi o tempo e em que volta isso ocorreu'''
    tupla = []
    for i in range(6):
        for j in range(10):
            if tempos[i][j] < tupla[1]:
                tupla = (i + 1, tempos[i][j], j + 1)
    return tupla