def melhor_volta(voltas):
    """Função que recebe como entrada uma matriz 6×10 com os
    tempos em segundos dos corredores em cada volta, e
    retorna uma tupla informando de quem foi a melhor volta
    da prova, com qual tempo e em que volta;
    list -> tuple"""
    # de quem foi a melhor volta?
    # qual foi o melhor tempo?
    # qual volta?
    melhor_piloto = min(voltas)
    melhor_volta = min(melhor_piloto)
    return ((voltas.index(melhor_piloto) + 1), melhor_volta, (melhor_volta.index(melhor_piloto) + 1))