def melhor_volta(matriz):
    '''Função que dada uma matriz 6x10 de entrada, sendo cada linha da matriz os tempo em segundos das 10 voltas dos 6 corredores. Retorna quem foi a melhor volta da prova, com qual tempo e em que volta''' 
    minimo = []
    for n in range(len(matriz)):
        minimo += [min(matriz[n])]
    melhor =list.index(minimo,min(minimo))
    volta = list.index(matriz[melhor],min(minimo))
    return melhor+1,min(minimo),volta+1