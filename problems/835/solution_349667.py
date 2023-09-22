def melhor_volta(matriz):
    #  lista de lista (matriz) --> tupla
    num_linhas = len(matriz)
    tempo_volta=matriz[0][0]
    de_quem=0
    qual_volta=0
    for i in range(0,num_linhas):
        num_colunas=len(matriz[i])
        for j in range(0,num_colunas):
            if matriz[i][j] < tempo_volta:
                tempo_volta = matriz[i][j]
                de_quem = i
                qual_volta = j
    return (de_quem+1, tempo_volta, qual_volta+1)