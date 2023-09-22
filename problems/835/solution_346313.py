def melhor_volta(matriz):
    """retorna de quem foi a melhor volta da prova, qual tempo e em qual volta
    list(list)->tuple"""
    b=[]
    for i in range(len(matriz)):
        list.append(b,min(matriz[i]))
    minimoT = min(b)
    corredor = list.index(b,min(b)) + 1
    volta = list.index(matriz[corredor-1],minimoT) +1
    return corredor, minimoT, volta