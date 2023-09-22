def melhor_volta(matriz_6x10):
    lista = []
    for corredor in range(1,7):
        list.append(lista, min(matriz_6x10[corredor - 1]))
    menor_tempo = min(lista)
    melhor_volta = list.index(lista, menor_tempo) + 1
    n_volta = list.index(matriz_6x10[melhor_volta - 1], menor_tempo) + 1
    return (melhor_volta, menor_tempo, n_volta)