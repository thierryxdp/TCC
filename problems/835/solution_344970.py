def melhor_volta(matriz):
    '''funcao que recebe uma matriz 6x10 com os tempos em segundo dos corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova, com o seu tempo e em qual volta
    matriz->tupla'''
melhortempo=()
if range(len(matriz))==6 and range(len(matriz[0]))==10:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            melhortempo= (min(matriz[i]),i)
		return melhortempo