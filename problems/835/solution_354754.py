def melhor_volta(matriz):
    '''funçao que dada uma matriz 6 x 10 simulando uma corrida de kart retorna qual corredor fez o menor tempo e a volta que ocorreu
    list -> tupla'''
    menor_tempo = []
    for indice in matriz:
        menor_tempo += [min(indice)]
    melhor_corredor = list.index(menor_tempo, min(menor_tempo))+1
    for elemento in matriz:
        for volta in elemento:
            if min(menor_tempo) == volta:
                melhor_volta = list.index(elemento, min(menor_tempo))+1
    return (melhor_corredor, min(menor_tempo), melhor_volta)