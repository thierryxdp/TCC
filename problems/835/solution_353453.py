def melhor_volta(tempos):
    '''funcao que recebe uma matriz 6 x 10 de tempos de voltas em uma pista de kart e retorna qual das voltas foi a mais rapida
    list->float'''
    matriz=(min(tempos))
    for x in range(6):
        for y in range(10):
              if tempos[x][y] < matriz[1]:
                     matriz = (x+1,tempos[x][y],y+1)
    return matri