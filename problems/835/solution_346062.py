def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta
       e retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em
       que volta.
       list -> tuple'''
    melhor = ()
    menor = []
    for i in matriz:
        x = min(i)
        list.append(menor,x)
    y = min(menor)
    for i in matriz:
        if y in i:
            melhor = (matriz.index(i)+1,y,i.index(y)+1)
    return melhor