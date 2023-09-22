def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(b,min(matriz[i]))
    for a in range(len(matriz)):
        for c in range(len(matriz[0])):
            if min(b)==matriz[a][c]:
                return (a+1,min(b),c+1)