def melhor_volta(matriz):

    voltas = []
    for i in matriz:
        voltas.append(min(i))

    menor_volta = min(voltas)
    index_min_volta = voltas.index(menor_volta)
        
    return (index_min_volta+1, menor_volta, matriz[index_min_volta].index(menor_volta)+1)