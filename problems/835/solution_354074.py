def melhor_volta(matriz):
    '''
    Funçao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em
    cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta, assumindo que os corredores tem tempos diferentes
    list(list) -> tuple
    '''
    m_corredor = []
    m_tempo = []
    volta = []
    for i in range(len(matriz)):
        tempo = min(matriz[i])
        list.append(m_tempo, tempo)
        for j in range(len(matriz[i])):
            if j == min(m_tempo):
                volta = list.index(matriz[(list.index(m_tempo,j))],j)
    return (i,min(m_tempo),volta)