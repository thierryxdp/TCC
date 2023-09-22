def melhor_volta(m):
    """Dada uma matriz 6x10 com tempos em segundos dos corredores em cada 
    volta, retorna uma tupla informando quem fez a melhor volta, com qual tempo
    e em que volta"""
    melhor = []
    for voltas in m:
        list.append(melhor,min(voltas))
    tempo = min(voltas)
    for x, voltas in enumerate(m,1):
        if tempo in voltas:
            kart = x
            volta = list.index(voltas,tempo) + 1
    return kart,tempo,volta