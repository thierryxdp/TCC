def melhor_volta(matriz):
    """
    Função para calcular a melhor volta de uma corrida, o piloto que fez está volta e em que volta foi feito esse tempo.
    matriz - é a matriz com as informações da corrida.
    list(list) --> tuple
    """
    n_linha = 6
    n_coluna = 10
    for i in range(n_linha):
        menor_tempo = min(i)
        if min(i) < menor_tempo:
            menor_tempo = min(i)
            piloto = i
    return piloto