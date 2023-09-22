from math import ceil
def melhor_volta(matriz):
    '''dada uma matriz 6x10 contendo o tempo de 6 corredores em 10 voltas, retorna uma tupla informando a melhor volta da prova, com qual tempo e em qual volta;
    list --> tuple'''
    todosostempos=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(todosostempos,matriz[i][j])
    tempominimo=min(todosostempos)
    if list.index(todosostempos,tempominimo)%10==9:
        volta=10
    else:
        volta=(list.index(todosostempos,tempominimo)+1)%10
    corredor=ceil((list.index(todosostempos,tempominimo)+1)/10)
    return (corredor,tempominimo,volta)