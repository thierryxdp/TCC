from math import ceil
def melhor_volta(matriz):
    '''funcao retorna a melhor volta e o piloto que a realizou. list->tupla'''
    count=[]
    a=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            count.append(matriz[i][j])
            if matriz[i][j]==min(count):
                a=(matriz[i].index(min(count)))+1       
    return ceil(count.index(min(count))/10),min(count),a