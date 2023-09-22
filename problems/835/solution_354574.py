def melhor_volta(matriz):
	"""Calcule e retorne uma tupla indicando de quem foi a melhor volta da
    prova, com qual tempo e em que volta, dado uma uma matriz de entrada
    6 x 10; list --> tuple"""
    melhor=[]
    for i in matriz:
        for j in i:
            melhor=melhor+[list.index(matriz,i),min(i),list.index(matriz, min(i))]
            melhor2=
                           return melhor