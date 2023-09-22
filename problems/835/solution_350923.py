def melhor_volta(matriz):
    
    menores = []
    for i in range(6):
        for j in range(10):
            x = matriz[i][j]
            if x == min(matriz[i]):
                menores += [x]
                melhor = min(menores)
                tupla = ((menores.index(melhor)+1),(melhor),(matriz[i].index(melhor)))
    return tupla