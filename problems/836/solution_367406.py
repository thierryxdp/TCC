def busca(setor, matriz):
    
    m = len(matriz)
    
    acumulador = []
    
    for i in range(m):
        if matriz[i][2] == setor:
            dado = matriz[i]
            acumulador += [dado[0:2] + dado[3]]
            
    return acumulador