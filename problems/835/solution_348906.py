def melhor_volta(matriz):
    voltas = []
    for i in range(7):
        for j in range(11):
            voltas.append(matriz[i][j])
            menor = min(voltas)
    return (i,menor,j)