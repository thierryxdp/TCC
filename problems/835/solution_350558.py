def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10 retorna as informacoes 
    de quem foi melhor na prova, com qual tempo e em que volta
    list -> tuple'''
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
	melhor_volta = min(lista)
    return (melhor_volta,)