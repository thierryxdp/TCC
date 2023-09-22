def melhor_volta(matriz):
    """ Essa função, dada uma matriz 6x10 com os segundos de 6 jogadores
	 em 10 voltas numa pista de Kart, calcula e retorna uma tupla informando
	 de quem foi a melhor volta da prova, em que tempo e em qual volta.
	list -> tuple"""
    
   
    lista = []
    
    for linha in matriz:
        for coluna in linha:
            list.append(lista, coluna)
    menor_tempo = min(lista)
    
    tupla = ()
	for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if menor_tempo == matriz[i][j]:
                tupla = tupla + (matriz[i])
             
    return tupla