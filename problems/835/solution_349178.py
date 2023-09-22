def melhor_volta(matriz: list)-> tuple:

    melhores_voltas = []
    voltas = []

    for i in range(6):
        list.append(melhores_voltas,min(matriz[i]))
        list.append(num_volta, list.index(matriz[i],min(matriz[i])))
        
    melhor_volta = min(melhores_voltas)
    num_volta = voltas[list.index(melhores_voltas,melhor_volta)] + 1
    corredor = list.index(melhor_volta) + 1

    return (corredor,melhor_volta,num_volta)