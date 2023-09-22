def melhor_volta(matriz):
    """ Essa função, dada uma matriz 6x10 com os segundos de 6 jogadores
	 em 10 voltas numa pista de Kart, calcula e retorna uma tupla informando
	 de quem foi a melhor volta da prova, em que tempo e em qual volta.
	list -> tuple"""
    
    lista = []
    for i in range(len(matriz)):
        lista.append(min(matriz[i]))
        menor_tempo = min(lista)
        
        if menor_tempo in matriz[i]:
            corredor = matriz.index(matriz[i])+1
            volta = matriz[i].index(min(lista))+1
            
    return (corredor, menor_tempo, volta)