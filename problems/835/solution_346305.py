def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    volta = 0
    for i in range(len(matriz)):
        volta += 1
        for j in range(len(matriz[0])):
            list.append(b,min(matriz[i]))

    minimoT = min(b)
    corredor = list.index(b,min(b)) + 1
    return corredor, minimoT, volta