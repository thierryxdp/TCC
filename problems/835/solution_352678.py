def melhor_volta(m):
    
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1,m[i][j],j+1)
    return tupla