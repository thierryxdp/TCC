def melhor_volta(m):
    '''Função que dada uma matrix 6x10 contendo o tempo em segundos de 6 corredores em 10 voltas, retorna de quem foi a melhor volta da prova, com qual tempo e em que volta.
       matriz->tuple'''
    ganhador = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if m[i][j] < tupla[1]:
                ganhador = (i+1,m[i][j],j+1)
    return ganhador