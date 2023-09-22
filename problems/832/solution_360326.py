def eh_quadrada (matriz):
    linhas=0.0
    elementos=0.0
    for i in range(len(matriz)):
        linhas+=1.0
        for j in range(len(matriz[0])):
            elementos+=1.0
    colunas=(elementos/linhas)
    if linhas==colunas:
        return True
    else:
        return False