def busca(setor, matriz):
    
    m = len(matriz)
    
    acumulador = []
    
    for i in range(m):
        if matriz[i][2] == setor:
            acumulador += [matriz[i]]
            
    return acumulador