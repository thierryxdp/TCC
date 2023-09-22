def melhor_volta(matriz):
    a = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append( a , matriz[i][j])
            tempo = min(a)
            if matriz[i][j] == tempo:
                kart = i
                volta = j
    return kart , tempo , volta