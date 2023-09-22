def melhor_volta(matriz):
    '''
    Funçao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em
    cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta, assumindo que os corredores tem tempos diferentes
    list(list) -> tuple
    '''
    m_tempo = []
    volta = 0
    for i in matriz:
        tempo = min(i)
        list.append(m_tempo, tempo)
        for j in matriz[i]:
            if j == tempo:
                volta = j
    return (i,m_tempo,volta)