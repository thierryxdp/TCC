def conta_numero(numero,matriz):
    
    
    
    n_vezes=0
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j]==numero:
                n_vezes = n_vezes+1
    return n_vezes