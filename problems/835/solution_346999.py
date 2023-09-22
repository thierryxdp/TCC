def melhor_volta(m):
    """
    informa qual a melhor volta dentre os corredores do kart
    """
    voltas=[]
    tempos=[]
    for i in range(len(m)):
        melhor=min(m[i])
        voltas.append((i+1,melhor,m[i].index(melhor)+1))
        tempos.append(melhor)
    menor=min(tempos)
    for i in range(len(voltas)):
        if menor==voltas[i][1]:
            return voltas[i]