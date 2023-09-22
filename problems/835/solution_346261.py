def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            a=min(matriz[i])
            d=list.append(b,a)
            c=min(d)
            if c==matriz[i][j]:
                return (j+1,a,i+1)