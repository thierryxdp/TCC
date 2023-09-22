def melhor_volta(matriz_tempos):

    tupla = (0,float('inf'),0)

    for volta in range(6):
        for tempo in range(10):
            if matriz_tempos[volta][tempo] < tupla[1]:

                tupla = (volta+1,matriz_tempos[volta][tempo],tempo+1) 

    return tupla