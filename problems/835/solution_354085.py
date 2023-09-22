def melhor_volta(matriz):
    '''
    Funçao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em
    cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta, assumindo que os corredores tem tempos diferentes
    list(list) -> tuple
    '''
    m_corredor = 1
    m_tempo = []
    volta = []
    ind = 1
    for i in range(len(matriz)):
        tempo = min(matriz[i])
        list.append(m_tempo, tempo)
        if min(m_tempo) in matriz[i]:
            m_corredor = i
        for j in range(len(matriz[i])):
            if j == min(m_tempo):
                ind = list.index(m_tempo,j)
                volta = list.index(matriz[ind],j)
    return (m_corredor,min(m_tempo),volta+1)