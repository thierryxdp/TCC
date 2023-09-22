def melhor_volta(matriz):
    '''retorna quem fez a melhor volta da prova, com qual tempo e em que volta, de acordo com uma matriz 6x10 (tempoxvolta) dada
    list -> tupla'''
    melhor_volta = -1
    melhor_tempo = -1
    melhor_corredor = ''
    n_volta = 0
    for volta in matriz:
        corredor = 1
        n_volta += 1
        for tempo in volta:
            corredor += 1
            if tempo > melhor_tempo:
                melhor_volta = n_volta
                melhor_tempo = tempo
                melhor_corredor = corredor
	return (melhor_corredor, melhor_tempo, melhor_volta)