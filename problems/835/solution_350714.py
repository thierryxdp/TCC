def melhor_volta(corrida):
    menor=min(corrida[0])
    veloz=1
    volta=corrida[0].index(menor)+1
    for corredor in range(1,6):
        if min(corrida[corredor])<menor:
            menor=min[corredor]
            veloz=corredor+1
            volta=corrida[corredor].index(menor)+1
    return (veloz,menor,volta)