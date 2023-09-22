def melhor_volta(matriz):
    tupla = ()
    voltas = []
    for i in range(6):
        for j in range(10):
            voltas.append(matriz[i][j])
            menor = min(voltas)
            if matriz[i][j] == menor:
                tupla = tupla + i
    return (i,menor)