def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10 retorna as informacoes 
    de quem foi melhor na prova, com qual tempo e em que volta
    list -> tuple'''
    lista = []
    for linha in matriz:
        for coluna in linha:
            lista.append(coluna)
	melhor_volta = min(lista)
    jogador = (list.index(lista,melhor_volta)//10) +1
    volta = 0
    for linha in matriz:
        if melhor_volta in linha:
        	for coluna in linha:
                volta+=1
                if coluna == melhor_volta
                	break
    
    return (jogador, melhor_volta, volta)