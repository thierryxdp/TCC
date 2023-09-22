def melhor_volta(matriz):
    '''Função que receba como entrada uma matriz de 6x10
    	com informações sobre uma rodada de kart, e retorne
        uma tupla dizendo quem, em que tempo e em que volta 
        foi o melhor. list --> tupla.'''
    lista = []
	for x in matriz:
        melhor_da_volta=min(x)
        lista.append(melhor_da_volta,x)
    melhor_volta = min(lista)
    vencedor = lista.index(melhor_volta)
    rodada = matriz[vencedor].index(melhor_volta)
    return vencedor + 1, melhor_volta, rodada + 1