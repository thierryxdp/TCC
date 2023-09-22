def melhor_volta(matriz):
    '''
    Funçao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em
    cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta, assumindo que os corredores tem tempos diferentes
    list(list) -> tuple
    '''
    m_tempo = []
    for i in matriz:
        for j in matriz[i]:
        tempo = min(i)
        list.append(m_tempo, tempo)
    return (i,m_tempo,j)