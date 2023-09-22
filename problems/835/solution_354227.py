def melhor_volta(matriz):
    """Função que recebe como entrada uma matriz 6×10 com os
    tempos em segundos dos corredores em cada volta, e
    retorna uma tupla informando de quem foi a melhor volta
    da prova, com qual tempo e em que volta;
    list -> tuple"""
    # de quem foi a melhor volta?
    # qual foi o melhor tempo?
    # qual volta?
    a = min(matriz)
    b = min(a)
    c = matriz.index(a)
    d = a.index(b)
    return ((c + 1), b, (d+1))