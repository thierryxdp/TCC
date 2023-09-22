def melhor_volta(matriz): #Entrada: Matriz (list)
    menor_tempo = min(matriz)
    corredor = matriz.index(menor_tempo)
    volta = matriz.index(min(menor_tempo))
    return (corredor + 1, min(menor_tempo), volta) #Saída: Tuple