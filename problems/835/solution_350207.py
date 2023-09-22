def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10 com
    os tempos em segundos dos corredores em 
    cada volta, retorna uma tupla informando 
    quem foi a melhor volta da prova, qual 
    o tempo e em que volta
    list -> tuple'''
    lista = []
    contador = 1
    for linha in matriz:
        for coluna in linha:
			lista.append(coluna)
	melhor_tempo = min(lista)
    for linha in matriz:
        for coluna in linha:
            contador +=1 
            if coluna == melhor_tempo:
                break 
	return (melhor_tempo, contador)