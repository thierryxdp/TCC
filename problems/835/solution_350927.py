def melhor_volta(matriz):
    """retorna uma tupla com que corredor fez a volta mais rapida, o tempo da volta e o numero da volta, respectivamente"""
    """list -> tuple"""
    
    menores = []
    for i in range(6):
        for j in range(10):
            x = matriz[i][j]
            if x == min(matriz[i]):
                menores += [x]
                melhor = min(menores)
                tupla = ((menores.index(melhor)+1),(melhor),(list.index((matriz[menores.index(melhor)]),(melhor))+1))
    return tupla