def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if min(matriz)==matriz[i][j]:
                return (i+1,min(matriz),j+1)