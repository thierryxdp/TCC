def melhor_volta(matriz):
    """ Funcao que recebe uma matriz 6 x 10.
    	Retorna uma tupla com informacoes de quem teve a melhor volta, qual tempo e em que volta;
        list -> tuple
    """
    menor_tempo = matriz[0][0]
    info = (0, menor_tempo, 0)
	for i in range(len(matriz)):
        if min(matriz[i]) < menor_tempo:
            menor_tempo = min(matriz[i])
            info = (0, menor_tempo, list.index(matriz[i], menor_tempo))
            
    return info