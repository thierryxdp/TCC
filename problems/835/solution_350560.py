def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10 retorna as informacoes 
    de quem foi melhor na prova, com qual tempo e em que volta
    list -> tuple'''
    lista = []
    i = 0
    j = 0
    for linha in matriz:
        lista.append(linha)
            
	melhor_volta = min(lista)
    
    return (melhor_volta,)