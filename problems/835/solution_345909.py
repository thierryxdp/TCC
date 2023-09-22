def melhor_volta(matriz):
    """Essa função identifica o melhor tempo e o exibe juntamente com a volta e o corredor
lista-->tupla"""
    lista = []
    x = 1
    for i in matriz:
        for c in i:
            list.append(lista,c)
    menor = min(lista)
    index = lista.index(menor)
    tempo = lista[index]
    if index < 10:
        x = 0
    corredor = int((str(index)[0]))+1
    volta = int((str(index)[x]))+1
    return (corredor, tempo, volta)