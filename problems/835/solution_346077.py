def melhor_volta(matriz):
    resp= [0, 0];
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < matriz[resp[0]] [resp[1]]:
                tempo= matriz[i][j];
                resp= [i,j];
                piloto= i+1;
                volta=j+1;
    return piloto, tempo, volta