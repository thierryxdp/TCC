def melhor_volta(matriz):
    """
    Função para calcular a melhor volta de uma corrida, o piloto que fez está volta e em que volta foi feito esse tempo.
    matriz - é a matriz com as informações da corrida.
    list(list) --> tuple
    """
    menor_tempo = 999
    piloto = 0
    for i in matriz:
        
        if min(i) < menor_tempo:
            melhor_piloto = matriz.index(matriz[piloto]) + 1
            menor_tempo = min(i)
            volta = i.index(min(i)) + 1
        piloto += 1
    return piloto, menor_tempo, volta