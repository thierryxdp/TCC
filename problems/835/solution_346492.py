import math
from math import floor
def melhor_volta(m):
    """Recebe uma matriz 'm' 6x10 com os 10 tempos em segundos dos 6 corredores e retorna uma tupla informando de quem foi a melhor volta da prova,com qual tempo e em que volta;list->tuple"""
    corredores=[]
    voltas=[]
    for i in range(6):
        corredores=corredores+m[i]
        for j in range(10):
            voltas=voltas+[m[i][j]]
    tempo=min(voltas)
    indice_volta=list.index(voltas,min(voltas))
    indice_corredor=floor((indice_volta)/10)
    tempo=min(voltas)
    return (indice_corredor+1,min(voltas),indice_volta+1)