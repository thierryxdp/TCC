def simetrica(x):
    

    for(i = 0; i < TAMANHO; i++){
        for(j = i + 1; j < TAMANHO; j++){
            if(matriz[i][j] != matriz[j][i])
                return 0