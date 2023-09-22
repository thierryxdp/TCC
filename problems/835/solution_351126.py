def melhor_volta(matriz):
    menor = 1
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < menor:
                menor = (i+1,matriz[i][j],j+1) #de quem, tempo, qual volta

    return menor , str.index(matriz, menor)