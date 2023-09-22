def melhor_volta(matriz):
    """A função recebe como entrada uma matriz com 6 linhas
    e 10 colunas (lista com 6 listas, cujos elementos são ints)
    e retorna uma tupla contendo 3 ints."""
	ts = []
    for tempos in matriz:
        for tempo in tempos:
            ts.append(tempo)  
    for i in range(9):
        for j in range(6):
            if min(ts) == matriz[j][i]:
    			return(j+1, min(ts), i+1)
    return (j-2, min(ts), i+2)