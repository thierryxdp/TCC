def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            a=min(matriz)
            if a==matriz[i][j]:
                return (j+1,a,i+1)