def melhor_volta(matriz):
"""Essa função identifica o melhor tempo e o exibe juntamente com a volta e o corredor
lista-->tupla"""
    lista = []
    for i in matriz:
        for c in i:
            list.append(lista,c)
    menor = min(lista)
    index = lista.index(menor)
    tempo = lista[index]
    corredor = int((str(index)[0]))+1
    volta = int((str(index)[1]))+1
    return (corredor, tempo, volta)