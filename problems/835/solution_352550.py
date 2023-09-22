def melhor_volta(matriz):
    '''Função que dada uma matriz 6x10 retorna de quem foi a melhor volta da prova,com qual tempo e em que volta. Todos os valores da matriz diferentes
     list->list'''
    C=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(C,matriz[i][j])
    menor=min(C)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==menor:
                quem=i+1
                volta=j+1
    return(quem,menor,volta)