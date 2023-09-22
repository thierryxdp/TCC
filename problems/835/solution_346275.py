def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=min(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if b==matriz[i][j]:
                return (i+1,b,j+1)