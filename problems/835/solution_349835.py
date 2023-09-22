def melhor_volta(matriz):
    '''Função que recebe como entrada um matriz 6 x 10 com os
    tempos em segundos dos 6 corredores nas 10 voltas de uma prova
    em uma pista de kart. A função retorna uma tupla informando de quem
    foi a melhor volta, com qual tempo e em que volta. list(list)->tuple'''
    tempos=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tempos.append(matriz[i][j])
    melhor_volta=min(tempos)
    for i in range(len(matriz)):
    	for j in range(len(matriz[0])):
            if matriz[i][j]==melhor_volta:
                corredor= i +1
                volta=j+1
    resultado=(corredor,melhor_volta,volta)
    return resultado