def melhor_volta(M):
    """Função que recebe como entrada uma matriz 6×10 com os
    tempos em segundos dos corredores em cada volta, e
    retorna uma tupla informando de quem foi a melhor volta
    da prova, com qual tempo e em que volta;
    list -> tuple"""
    a = min(M)
    b = min(a)
    return ((M.index(a) + 1), b, (a.index(b) + 1))