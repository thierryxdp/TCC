def melhor_volta(matriz):
    
    tupla = () 
    menores = []
    for i in range(6):
        for j in range(10):
            if matriz[i][j] == min(matriz[i]):
                menores.append(matriz[i][j])
                tupla += ((menores.index(min(menores))),(min(menores)),)
    return tupla