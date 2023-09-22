def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    for i in range(len(matriz)):
        list.append(b,min(matriz[i]))
        for j in range(len(matriz[0])):
            if min(b)==matriz[i][j]:
                return (i+1,min(b),j+1)