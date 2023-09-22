def melhor_volta(matriz):
    """ Essa função, dada uma matriz 6x10 com os segundos de 6 jogadores
	 em 10 voltas numa pista de Kart, calcula e retorna uma tupla informando
	 de quem foi a melhor volta da prova, em que tempo e em qual volta.
	list -> tuple"""
    
    lista = []
    lista_2
    for linha in matriz:
        for coluna in linha:
            list.append(lista, coluna)
    menor_tempo = min(lista)
    
    for linha in matriz:
        for coluna in linha:
            if menor_tempo in coluna:
                list.append(lista_2, coluna)
    
    return lista