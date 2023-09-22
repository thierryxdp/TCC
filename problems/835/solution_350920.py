def melhor_volta(matriz):
    
    tupla =()
    menores = []
    for i in range(6):
        for j in range(10):
            x = matriz[i][j]
            if x == min(matriz[i]):
                menores += [x]
                melhor = min(menores)
                tupla += ((i + 1),(melhor),(j + 1))
    return tupla