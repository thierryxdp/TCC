def melhor_volta(matriz):
    '''retorna quem teve a melhor volta. list(list)->tuple'''
    s = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            s.append(matriz[x][y])
    menor = min(s)
    corredor = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if menor in matriz[x][y]:
                corredor.apeend(matriz[x])
                a = list.index(corredor,menor)
                return (x,menor,a)