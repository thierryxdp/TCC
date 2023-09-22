def melhor_volta(matriz):
    m = min([valor for linha in matriz for valor in linha])
    l = 0
    c = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i][j] == m:
                l = i+1
                c = j+1
    return l, m, c