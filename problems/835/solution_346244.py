def melhor_volta(m):
    """Recebe uma matriz no formato lista de listas 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando: De quem foi a melhor volta,com qual tempo e em que volta;list->tuple"""
    
    for i in range(6):
        corredores=m[i]
        for j in range(10):
            voltas=m[i][j]
    return min(voltas)