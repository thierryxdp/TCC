def melhor_volta(matriz6x10):
    vencedor = (0,float('inf'),0)
    for corredor in range(1,6):
        for volta in range(1,10):
            if matriz6x10[corredor][volta]<vencedor[1]:
                vencedor=(corredor+1, matriz6x10[corredor][volta],volta+1)
    return vencedor