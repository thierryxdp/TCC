def melhor_volta(matriz):
    """dado uma matriz que representa o tempo em 10 voltas de kart
    de 6 corredores, retorna a melhor volta de todas, qual foi seu tempo
    e em qual volta; list[list[float]]->tupla(int,float,int)"""
    melhor=matriz[0][0]
    corredor=0
    volta=0
    for i in range(1,7):
        if min(matriz[i-1])<melhor:
            melhor=min(matriz[i-1])
            corredor=i
            volta=matriz[i-1].index(melhor)+1
    return (corredor,melhor,volta)