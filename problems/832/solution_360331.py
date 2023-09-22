def eh_quadrada (matriz):
    linhas=0
    elementos=0
    for i in range(len(matriz)):
        linhas+=1
        for j in range(len(matriz[0])):
            elementos+=1
    colunas=(elementos/linhas)
    if linhas==colunas:
        return True
    else:
        return False