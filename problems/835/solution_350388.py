def melhor_volta(matriz):
    """funcao que recebe uma matriz 6x10 representando os tempos de 6 corredores nas 10 voltas de uma corrida de kart e retorna tupla que informa de quem foi a melhor volta da prova, com qual tempo e o numero da volta;
       list->tuple"""
    tempos=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempos.append(matriz[i][j])
            menor=min(tempos)
            if menor==matriz[i][j]:
                posicao1=i
                posicao2=j
    return (posicao1+1,menor,posicao2+1)