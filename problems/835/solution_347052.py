def melhor_volta(matriz):
    cont = 0
    pos = 0
    for i in range(6):
        cont = 0
        for j in range(10):
            if len(matriz[pos]) == min(min(matriz)):
                tupla = (i+1,matriz[i][j],j+1)
                cont = cont + 1
            pos = pos + 1
    return tupla