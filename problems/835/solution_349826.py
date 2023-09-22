def melhor_volta(matriz):
    '''Função que recebe como entrada um matriz 6 x 10 com os
    tempos em segundos dos 6 corredores nas 10 voltas de uma prova
    em uma pista de kart. A função retorna uma tupla informando de quem
    foi a melhor volta, com qual tempo e em que volta. list(list)->tuple'''
    melhor_volta = min(tempos)
    for i in range(1,len(matriz)+1):
        for j in range(1,len(matriz[0]+1)):
            tempos.append(matriz[i][j])
    melhor_volta=min(tempos)
     for i in range(1,len(matriz)+1):
        for j in range(1,len(matriz[0]+1)):
            if matriz[i][j]=melhor_volta:
                corredor= i
                volta=j
    resultado=(corredor,melhor_volta,volta)
    return resultado