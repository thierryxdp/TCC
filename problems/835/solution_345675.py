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
            if menor == matriz[x][y]:
                corredor.append(matriz[x])
                a = y
                return (x+1,menor,a)