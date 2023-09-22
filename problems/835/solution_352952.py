def melhor_volta(matriz):

    '''
    Função que recebe uma matriz como parâmetro e retorna
    a média dos termos da mesma.

    none -> float
    '''

    lin = len(matriz)
    col = len(matriz[0])
    d = []
    tempo = []
    for i in range(lin):
        m = []
        for j in range(col):
            m.append(matriz[i][j])
        d.append(m)
    
    li2 = []
    tam = len(d)
    for x in range(tam):
        mini = min(d[x])
        li2.append(mini)
    tempo.append(min(li2))

    for y in range(lin):
        if matriz[y] in d:
            corredor = y

    for z in range(col):
        if matriz[z] in d:
            volta = z-1

    return (cooredor,tempo,volta)