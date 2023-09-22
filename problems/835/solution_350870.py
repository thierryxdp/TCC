def melhor_volta(matriz:list)->tuple:
    '''diz a melhor volta: de quem foi, qual o número da volta e o tempo da volta'''
    melhor=0
    tempo=10000
    corredor=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if tempo>matriz[i][j]:
                tempo=matriz[i][j]
                melhor=matriz[i].index(matriz[j])+1
                corredor=i+1
    return (corredor,tempo,melhor)