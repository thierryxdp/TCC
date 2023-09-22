def melhor_volta(matriz):
    '''Dada uma matriz, retorne uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta;
    list -> tuple'''
    menor=500
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j]<menor:
                menor=matriz[i][j]
                n=i
                v=j
    return (n+1,menor,j+1)