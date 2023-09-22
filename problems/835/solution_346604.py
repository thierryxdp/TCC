def melhor_volta(matriz):
    
    m = len(matriz)
    n = len(matriz[0])
    
    acumulador = []
    
    for i in range(m):
        for j in range(n):
            acumulador += [matriz[i][j]]
    
    minimo = min(acumulador)
    
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == minimo:
                corredor = i + 1
                volta = j + 1
    
    return corredor, minimo, volta