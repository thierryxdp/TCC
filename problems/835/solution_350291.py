def melhor_volta(matriz):
    """funcao que recebe uma matriz 6x10 representando os tempos de 6 corredores nas 10 voltas de uma corrida de kart e retorna tupla que informa de quem foi a melhor volta da prova, com qual tempo e o numero da volta;
       list->tuple"""
    minimo=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            minimo=min(matriz[i])
            if matriz[i][j]==minimo:
    return (i,matriz[i][j],j)