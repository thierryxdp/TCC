def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    i=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(b,min(matriz[i]))
    i+=1
            if min(b)==matriz[i][j]:
                return (i+1,min(b),j+1)