def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        a=min(matriz[i])
            list.append(b,a)
            if min(b)==matriz[i][j]:
                return (i+1,min(b),j+1)