def melhor_volta (mat):
    '''função que dada uma matriz com tempos em segundos das voltas de cada corredor retorna de quem foi a melhor
    volta, com qual tempo e em que volta; list->tuple'''
    tempo= 100000
    tupla=(0,tempo)
    for i in range(6):
        for j in range(10):
            if mat[i][j]<tupla[1]:
                tupla=(i+1,mat[i][j],j+1)
    return tupla