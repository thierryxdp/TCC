def melhor_volta(m):
    '''
    Recebe como entrada uma matriz 6x10 com tempos de corredores de Kart.
    (linha 0 = corredor 1 e coluna 0 = volta 1) e devolve em uma tupla o corredor com o melhor
    tempo, a volta e o tempo.
    
    Entrada/Saida:
    list -> tuple(int, float, int)
    '''
    volta = -1
    minimo = m[0][0]
    corredor = -1
    
    for i in m:
        if min(i) < minimo:
            minimo = min(i)
            volta = i.index(minimo)
			corredor = m.index(i)
	return (corredor + 1, minimo, volta + 1)