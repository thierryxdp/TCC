def melhor_volta(tempos):
    '''funcao que recebe uma matriz 6 x 10 de tempos de voltas em uma pista de kart e retorna qual das voltas foi a mais rapida
    list->float'''
    matriz=(0,tempos)
    for x in range(6):
        for y in range(10):
              if tempos[x][y] < tupla[1]:
                     tupla = (x+1,matriz_tempos[x][y],y+1)
    return tupla