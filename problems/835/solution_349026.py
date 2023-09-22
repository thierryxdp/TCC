def melhor_volta(matriz):
    ''' Dado uma matriz 6x10 com os tempos em segundos dos
    	corredores em cada volta, retorna uma tupla informando
        de quem foi a melhor volta da prova, com qual tempo e
        em que volta
        list -> tuple
     '''
    #n_linhas = len(matriz)
    #n_colunas = len(matriz[0]))
    tupla = ()
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
	lista.sort()
    melhor_tempo = lista[-1]
    for i in range(len(matriz)):
        corredor = (lista[i].index(melhor_tempo))+1
    for j in range(len(matriz[0])):
        volta = (lista[j].index(melhor_tempo))+1
    tupla += (corredor,)
    tupla += (melhor_tempo,)
    tupla += (volta,)