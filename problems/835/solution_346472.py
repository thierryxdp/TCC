def melhor_volta(m):
    """Recebe uma matriz 'm' 6x10 com os 10 tempos em segundos dos 6 corredores e retorna uma tupla informando de quem foi a melhor volta da prova,com qual tempo e em que volta;list->tuple"""
    corredor=min(m)
    indice_corredor=list.index(m,corredor)
    volta=list.index(m[indice_corredor],min(m[indice_corredor]))
    tempo=min(m[indice_corredor])
    return (indice_corredor+1,tempo,volta+1)