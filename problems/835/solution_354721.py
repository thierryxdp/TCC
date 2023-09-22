def melhor_volta(matriz):
    menor_temp = volta = vencedor = 1000
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if min(matriz[i][j],menor_temp)==matriz[i][j]:
                menor_temp = min(matriz[i][j],menor_temp)
                vencedor = i + 1
                volta = j + 1
    return vencedor, menor_temp, volta