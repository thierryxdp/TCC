def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz 6x10 com os tempos em segundos
    dos corredores em cada volta e retorna uma tupla informando de quem foi a
    melhor volta da prova, com qual tempo e em que volta.
    list(list)-->tup(int,float,int)'''
    menortempo = 1000000000000000
    volta = 0
    corredor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if menortempo > matriz[i][j]:
                menortempo = matriz[i][j]
                corredor = i+1
                volta = j+1
    return (corredor,menortempo,volta)