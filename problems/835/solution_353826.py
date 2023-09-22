def melhor_volta(matriz6x10):
    '''função que dada uma matriz 6 por 10,representando os 
    corredores e as voltas de uma corrida respectivamente,
    retorna uma tupla dizendo quem foia melhor volta,o tempo e
    em qual volta; list->tuple'''
    resp=10000
    resp2=0
    for i in range(len(matriz6x10)):
        for j in range(len(matriz6x10[0])):
            if matriz6x10[i][j]<=resp:
                resp=matriz6x10[i][j]
                resp2=(i+1,(matriz6x10[i][j]),j+1)
    return resp2