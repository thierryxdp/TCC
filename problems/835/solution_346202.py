def melhor_volta(matriz):
    corredor_1 = min(matriz[0])
    corredor_2 = min(matriz[1])
    corredor_3 = min(matriz[2])
    corredor_4 = min(matriz[3])
    corredor_5 = min(matriz[4])
    corredor_6 = min(matriz[5])
    corredores = [corredor_1,corredor_2,corredor_3,corredor_4,corredor_5,corredor_6]
    corredor = 0
    while corredor in range(len(matriz)):
        corredor_atual = min(corredores)
        if corredor_atual in matriz[corredor]:
            volta = list.index(matriz[corredor], corredor_atual)
            corredor = corredor + 1
            return (corredor, corredor_atual , volta + 1)